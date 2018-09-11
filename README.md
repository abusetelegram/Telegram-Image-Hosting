# Telegram-Image-Hosting

使用 Telegram 做图床

## 说明

Telegram 在之前推出了频道消息嵌入到网页的插件，这使得图片，视频都可以使用 Telegram 的 CDN 进行分发并嵌入到自己的页面中。

这个工具可以让你方便的提取图片，视频的固定链接

## 优劣

### 优点

- 永久储存
- 频道+hashtag 方便管理资源

### 缺点

- CDN 对于国内不友好（你懂的）
- 色情内容等频道会被屏蔽（比如： ![https://t.me/maito_channel/3537?embed=1](https://cdn5.telesco.pe/file/tHAwEgdXGNT6ba9l9tRniqhEqIy8OJUWDN48_NQFGOHZyNv4REjJzLQdfnE39Bqs64GcblmLLTRG8IgpyoBqA1jru6W5VlbColwf1n_d6x1O1xga5aORIONIFJLSLrEJbaHDba44tTnXSdevdxsLhZ__DAW8eFNy9gRQa6PMA90jp1wWcGW0PPVn2QLhX4hmskM9r1hVW_l3F33Dvf8sd2w-caAsLedkTcpz7D3ojcN1MxEbhgL3Ir7OvxHWK-u9GQNXylmJO9mRHAJDHtTCWd8r_HT77NV8yCOebOETWvBLPKRfvNEdoEblQ_65a7E8sAXIcMFKAszhgs9TLup8hw.jpg) https://t.me/maito_channel/3537?embed=1
- 对于长图支持不好（会被压缩）

## 使用

- 在公开频道或群组上面发送需要的图片
- 复制链接 ![](https://cdn5.telesco.pe/file/hpW7rdsChXsF73vIqaDfFcX_opEWQ-ki3SxIauiuiS6Av-335hVTNdWrg6kVaFZXThEVEaoK3zD6lAccevwa63CFEU5bDIh1Vdzw7IwG3Egd95NYxw0dwz7Mq1YZiDJT9f2xXCUffvYs75akUws4yhx0VThRgqI9MEddiPizrlI7-zZybMdLiVGbQjHFGMjfz_tFBk1cZbo8NbIuvmJ1xVbAv_7po-oglbMXNIYQQXuZB0Bqsrh9ppHYEz7f9Pd78NfKFiMhyrpsKqdVOuNpfwt6mx73gMivb2h2aIYjulA0gFVFAf4-g_Nfl36_wTsTfVIGcoVZZ3hJG19WxeaWSg.jpg)
- 在 https://telegram-image-hosting.never.pet （国内用户建议自带梯子）粘贴
- 获得链接

## 原理

`embed?=1` 参数访问时会带上所有图片和视频资源的链接

## 其他相关内容

- [python 脚本](telegram-image-hosting.py)

## P.S.

- 目前测试删除消息后图片依然会存在一段时间。[测试链接，如果404了就是没了，与 11/09/2018 13:47 UTC-4 删除](https://cdn5.telesco.pe/file/EdZ_YtmT9X-Pt4ASXTeip4drCR9XFn92Tc8f50gAq0gUb-dPZ8tFPMhcKg8cdrBJXm-LwYV24nfFsUfoFqqZZjviHHyDgwp5ebzrGVqhYAT8prY8Z7JZagLygAyxf7ZjQjYGoBS5rO9FXHUYaYj0Xo1e4WYWxlf6kaC-cshzGnCMbKYzZDiDpJmH7sPZq6g9Yj6G47AjwZIzuAv8MZKpnmbY8HGRKooPCl5Csur6VXh41Lv1eJWy1vpy_-1lLhXgFkUCWNVlKQ7wN2Td3ViFzP6oFuTzVo8Jf1yTGyBHRXRBmVzZ-W1IjnkfDAHUDHJPGJUABYm_gJmozZRgxLM5BQ.jpg)
