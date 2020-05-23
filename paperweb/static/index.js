layui.use(['element', "layer", "jquery", "form"], function () {
    var element = layui.element;
    var form = layui.form;
    var layer = layui.layer;
    var $ = layui.jquery;
    var path = "http://127.0.0.1:5000";
    //var path = "http://134.175.190.199:5000";

    element.on('tab(docDemoTabBrief)', function (data) {
        //console.log(this); //当前Tab标题所在的原始DOM元素
        //console.log('test')
        layer.msg('切到了' + this.innerText, {time: 1000});
        //console.log(data.index); //得到当前Tab的所在下标
        //console.log(data.elem); //得到当前的Tab大容器
    });

    form.on('submit(rsainit)', function (data) {
        //layer.msg(JSON.stringify(data.field));
        var url = path + '/rsaInit.do';
        var indexload;
        //console.log(1)
        $.ajax({
            url: url,
            type: "post",
            data: JSON.stringify({
                'n': data.field.n,
            }),
            dataType: "json",
            beforeSend: function () {
                indexload = layer.load(0, {shade: false}); //0代表加载的风格，支持0-2
                //$("#button1").addClass("div-cant-click")
                $("#button1").html("正在处理中...");
                $("#button1").attr("disabled", "disabled");
            },
            success: function (data) {
                console.log("传过来的是：", data);
                layer.close(indexload);
                $("#button1").html("生成公钥私钥");
                $("#button1").removeAttr("disabled");
                layer.msg('公私钥生成成功', {
                    icon: 1,
                    time: 2000
                }, function () {
                    window.location.reload()
                });
                //$("#button1").removeClass("div-cant-click")
            },
            error: function () {
                console.log("ajax请求失败");
            }
        });
        return false;
    });
    
    form.on('submit(rsaSigGen)', function (data) {
        //layer.msg(JSON.stringify(data.field));
        var url = path + '/rsaSigGen.do';
        var indexload;
        console.log(data.field)
        if (data.field.flagakr == 'on') {
            var flagakr = 'True'
        } else {
            var flagakr = 'False'
        }
        //console.log(flagakr)

        var id_array = new Array();
        $('.userchoose:checked').each(function () {
            id_array.push($(this).val());//向数组中添加元素
        });
        var userstr = id_array.join(',');//将数组元素连接起来以构建一个字符串

        $.ajax({
            url: url,
            type: "post",
            data: JSON.stringify({
                'k': data.field.k,
                'ms': data.field.ms,
                'flagakr': flagakr,
                'userstr': userstr
            }),
            dataType: "json",
            beforeSend: function () {
                indexload = layer.load(0, {shade: false, time: 10 * 1000}); //0代表加载的风格，支持0-2
            },
            success: function (data) {
                //console.log("传过来的是：", data);
                layer.close(indexload);
                layer.msg('环签名生成成功', {
                    icon: 1,
                    time: 2000
                });
                //给表单赋值
                form.val("rsaSigGenMs", {
                    "rsaSig": data.data,
                });
            },
            error: function () {
                console.log("ajax请求失败");
            }
        });
        return false;
    });

    form.on('submit(formDemo3)', function (data) {
        var url = path + '/rsaVerifySig.do';
        var indexload;
        //console.log(1)
        $.ajax({
            url: url,
            type: "post",
            data: JSON.stringify({
                'vsm': data.field.vsm,
                'vssigma': data.field.vssigma,
            }),
            dataType: "json",
            beforeSend: function () {
                indexload = layer.load(0, {shade: false, time: 10 * 1000}); //0代表加载的风格，支持0-2
            },
            success: function (data) {
                console.log("传过来的是：", data);
                layer.close(indexload);
                if (data.data == 'true') {
                    layer.msg('验证完成，结果为' + data.data, {
                        icon: 1,
                        time: 2000
                    });
                } else {
                    layer.msg('验证完成，结果为' + data.data, {
                        icon: 2,
                        time: 2000
                    });
                }
                //给表单赋值
                form.val("rsaVerifySig", {
                    "answer1": data.data,
                });
            },
            error: function () {
                console.log("ajax请求失败");
            }
        });
        return false;
    });

    form.on('submit(formDemo4)', function (data) {
        var url = path + '/rsaVerifyRelevance.do';
        var indexload;
        //console.log(1)
        $.ajax({
            url: url,
            type: "post",
            data: JSON.stringify({
                'vrsigma1': data.field.vrsigma1,
                'vrsigma2': data.field.vrsigma2,
            }),
            dataType: "json",
            beforeSend: function () {
                indexload = layer.load(0, {shade: false, time: 10 * 1000}); //0代表加载的风格，支持0-2
            },
            success: function (data) {
                console.log("传过来的是：", data);
                layer.close(indexload);
                if (data.data == 'true') {
                    layer.msg('验证完成，结果为' + data.data, {
                        icon: 1,
                        time: 2000
                    });
                } else {
                    layer.msg('验证完成，结果为' + data.data, {
                        icon: 2,
                        time: 2000
                    });
                }

                //给表单赋值
                form.val("rsaVerifyRe", {
                    "answer2": data.data,
                });
            },
            error: function () {
                console.log("ajax请求失败");
            }
        });
        return false;
    });


    form.on('submit(formDemo5)', function (data) {
        var url = path + '/rsaSigConvert.do';
        var indexload;
        var cuser = data.field.cuser;
        $.ajax({
            url: url,
            type: "post",
            data: JSON.stringify({
                'cuser': data.field.cuser,
                'csigma': data.field.sigma5,
            }),
            dataType: "json",
            beforeSend: function () {
                indexload = layer.load(0, {shade: false, time: 10 * 1000}); //0代表加载的风格，支持0-2
            },
            success: function (data) {
                //console.log("传过来的是：", data);
                layer.close(indexload);
                if (data.data == 'true') {
                    layer.msg('验证成功，输入的环签名是由编号'+cuser+'的成员生成', {
                        icon: 1,
                        time: 2000
                    });
                } else {
                    layer.msg('验证失败，输入的环签名不是由编号'+cuser+'的成员生成', {
                        icon: 2,
                        time: 2000
                    });
                }
                //给表单赋值
                form.val("rsaConvertSig", {
                    "answer3": data.data,
                });
            },
            error: function () {
                console.log("ajax请求失败");
            }
        });
        return false;
    });


    $(".tip-a").mouseenter(function () {
        var that = this;
        layer.tips('在输入成员数后，会为这些成员生成各自的公钥pk和私钥sk', that);
    });
    $(".tip-b").mouseenter(function () {
        var that = this;
        layer.tips('1. 输入当前签名者编号' + '</br>' +
            '2. 关联标签的选择可让同一签名者生成的两个签名保持关联性' + '</br>' +
            '3. 环成员选择代表了当前签名者在哪一个环中生成签名' + '</br>' +
            '4. 输入的消息表示为这个消息生成环签名'
            , that);
    });
    $(".tip-c").mouseenter(function () {
        var that = this;
        layer.tips('输入消息和生成的环签名点击环签名验证按钮，验证签名的合法性', that);
    });
    $(".tip-d").mouseenter(function () {
        var that = this;
        layer.tips('输入两个签名，点击关联性验证按钮判断两者是否具有关联性', that);
    });

    $(".tip-e").mouseenter(function () {
        var that = this;
        layer.tips('选择待判断的签名者，输入环签名，判断该环签名是否由其生成', that);
    });
});

