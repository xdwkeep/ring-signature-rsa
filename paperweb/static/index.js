layui.use(['element', "layer", "jquery", "form"], function () {
    var element = layui.element;
    var form = layui.form;
    var layer = layui.layer;
    var $ = layui.jquery;
    var path = "http://127.0.0.1:5000";

    console.log('test')

    $(".gsget").on("click", function () {
        var url = path + "/getgs.do";
        // console.log("请求controller的url是:" + url)
        $.ajax({
            url: url,
            type: "post",
            data: {
                'userid': userid,
            },
            dataType: "json",
            success: function (data) {
                // console.log("传过来的是：")
                // console.log(data)
                layer.msg('公私钥生成成功', {
                    icon: 1,
                    time: 1500
                });

            },
            error: function () {
                console.log("ajax请求失败");
            }
        });
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

