layui.use(['element', "layer", "jquery", "form"], function () {
    var element = layui.element;
    var form = layui.form;
    var layer = layui.layer;
    var $ = layui.jquery;
    var path = "http://127.0.0.1:5000";

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
            },
            success: function (data) {
                console.log("传过来的是：", data);
                layer.close(indexload);
                layer.msg('公私钥生成成功', {
                    icon: 1,
                    time: 2000
                });
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
        console.log(1)
        $.ajax({
            url: url,
            type: "post",
            data: JSON.stringify({
                'k': data.field.k,
                'ms': data.field.ms,
            }),
            dataType: "json",
            beforeSend: function () {
                indexload = layer.load(0, {shade: false, time: 10*1000}); //0代表加载的风格，支持0-2
            },
            success: function (data) {
                console.log("传过来的是：", data);
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
        layer.msg(JSON.stringify(data.field));
        return false;
    });

    form.on('submit(formDemo4)', function (data) {
        layer.msg(JSON.stringify(data.field));
        return false;
    });

});

