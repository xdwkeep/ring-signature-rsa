layui.use(['element', "layer", "jquery", "form"], function () {
    var element = layui.element;
    var form = layui.form;
    var layer = layui.layer;
    var $ = layui.jquery;
    //var path = "http://127.0.0.1:5000";
    var path = "http://134.175.190.199:5000";

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

});

