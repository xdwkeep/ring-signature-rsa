layui.use(['element', "layer", "jquery", "form"], function () {
    var element = layui.element;
    var form = layui.form;
    var layer = layui.layer;
    var $ = layui.jquery;
    var path = "http://127.0.0.1:5000";
console.log(0)
    form.on('submit(rsainit)', function (data) {
        //layer.msg(JSON.stringify(data.field));
        var url = path + '/rsaInit.do';
        console.log(1)
        $.ajax({
            url: url,
            type: "post",
            data: JSON.stringify({
                'n': data.field.n,
            }),
            dataType: "json",
            success: function (data) {
                console.log("传过来的是：")
                console.log(data)
                layer.msg('公私钥生成成功', {
                    icon: 1,
                    time: 1500
                });
            },
            error: function () {
                console.log("ajax请求失败");
            }
        });
        return false;
    });


    form.on('submit(formDemo2)', function (data) {
        layer.msg(JSON.stringify(data.field));
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

