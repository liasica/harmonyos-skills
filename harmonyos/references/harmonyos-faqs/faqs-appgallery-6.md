---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-appgallery-6
title: AGC页面菜单缺失或点击菜单报错问题排查指导
breadcrumb: FAQ > 应用服务开发 > 应用市场服务（AppGallery Kit） > AGC页面菜单缺失或点击菜单报错问题排查指导
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:50+08:00
doc_updated_at: 2026-08-26
content_hash: sha256:d2834234290eecce28a95041ee1d3d16d5309f977ad7744f694e8dc81e904040
---

## 问题现象

登录AGC页面进行操作时，有些菜单看不到、按钮点击无响应，无法进行下一步操作。比如邀请测试无法找到对应的"测试用户"菜单、发布应用时没有"提交审核"按钮、点击某些菜单会未知错误、点击某些菜单无响应等。

* 缺少提交审核按钮：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/J-1qlKZRTSKFh9UeDFKyrw/zh-cn_image_0000002690046132.png "点击放大")
* 缺少"测试用户"菜单；

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/L8HZF58JSMyvF5TwUeue6Q/zh-cn_image_0000002719885699.png "点击放大")
* 点击菜单报未知错误：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/9x4Kyb8WT6iPkiCYre3mgA/zh-cn_image_0000002690206004.png "点击放大")
* 点击"应用分类"设置按钮无响应：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6e/v3/jKIN9GsMRHqHlofAt4E9Vw/zh-cn_image_0000002719885701.png "点击放大")

## 背景知识

1. AGC是上架分发的入口，包含应用、项目、证书、个人信息等多个菜单栏，缺少部分菜单会影响开发者的操作。
2. AGC的菜单展示依赖于登录的账号角色和权限，为方便管理，AGC提供了团队账号的功能，主账号可以根据成员的职责配置不同的角色。最高权限角色为"系统管理员"，其次还有"APP管理员"、"运营"、"客服"、"法务"等角色。不同角色又对应不同的权限，如"APP管理员"可以进行应用上架分发和测试，"运营"角色负责应用运营数据查看，"法务"角色负责协议签署等，具体可以参见[角色与权限列表。](../app/agc-help-rolepermission-0000001155345429.md)
3. 为了方便进行页面的自定义布局，AGC还提供了菜单自定义功能，可以选择部分菜单展示或隐藏。

## 问题定位

1. 排查是否团队账号权限问题。
   * 可以登录AGC，进入"用户与访问-个人信息"可以查看当前是否是团队账号，是何种角色，拥有哪个项目和应用的权限。
   * 登录的账号角色是"账号持有者"，即主账号，拥有最高权限。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/BpX5bMrgQemu4fSj1Q9Akg/zh-cn_image_0000002719768367.png "点击放大")
   * 登录的账号角色是"运营"、"开发"和"客服"，只能进行数据查看，不能进行应用上架。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/QNZGYZ8QRryVvUUOmsJMZQ/zh-cn_image_0000002719769101.png "点击放大")

2. 排查是否进行了自定义菜单权限。AGC左下角有自定义菜单功能，选中的菜单右边的图钉时会展示菜单，不选中不展示。如"测试用户"菜单未选中时，左侧菜单栏不展示。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/sgxHHtC7RrCFvLQ4kklJNw/zh-cn_image_0000002690049642.png "点击放大")
3. 出现未知错误时，可以通过浏览器日志来获取具体的报错原因，打开浏览器日志（一般是按F12）->进入Network->选中报错的接口->查看报错信息描述。

## 分析结论

1. 排查是否是团队账号登录的AGC，如果是主账号，继续排查是否是进行了自定义菜单导致。
2. 如果不是团队账号，查看角色是否合理，建议一般至少"APP管理员"以上才可以进行应用上架测试。联系主账号，将角色提高至"APP管理员"或者"管理员"。

## 修改建议

1. 登录[AGC平台首页](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html#/)，通过右上角个人账号位置点击[个人信息](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html#/ups/9249519184595931321)，在"角色管理"页签查看当前是否为团队账号，是何种角色，拥有哪个项目和应用的权限。建议至少"APP管理员"以上才具备应用管理权限，拥有上架测试、应用分类设置等权限。
2. 在AGC左下角自定义菜单功能，查看是否没选择对应的菜单，如"测试用户"，如没选中，选中即可。![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a/v3/ErYi4iYkQNese788fZIL5g/zh-cn_image_0000002719893471.png "点击放大")
3. 若出现未知错误，也可以通过浏览器日志查看是否是当前登录用户没有权限导致，如果使用了团队账号登录，登录的角色可能是开发或者运营，建议联系账号持有者提高权限，一般至少需要提高至APP管理员角色。然后退出账号重新登录再试一下。

## 常见FAQ

Q：APMS上选择忽略SDK报错后刷新仍显示处理中，如何解决？

A：该问题为账号权限不足导致。经实际验证，APMS的忽略操作仅"APP管理员"或主账号权限可执行，子账号若仅有"运营"或"客服"角色则无法完成该操作。需联系主账号为该子账号赋予"APP管理员"及以上权限，角色与权限说明参见[角色与权限列表](../app/agc-help-rolepermission-0000001155345429.md)。
