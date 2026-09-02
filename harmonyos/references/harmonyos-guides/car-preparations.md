---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/car-preparations
title: 开发准备
breadcrumb: 指南 > 系统 > 硬件 > Car Kit（车服务） > 开发准备
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:37+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:2df539ddb58e4716fe74da8f5cf3fbb6e812fa1efef179efb60db9dcc8bdbc71
---

应用在使用Car Kit能力前，开发者需要完成的配置：配置编译模式、配置权限、配置能力。

## 配置编译模式

在打包应用时，请在DevEco Studio中，点击右上角![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/-eICjmHaQT-b3fM3SLGoKA/zh-cn_image_0000002706674462.png)图标，将编译模式修改为“release”，然后点击右下角的“Apply”即可。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ff/v3/WorVT79RQ0mIGp243hgywQ/zh-cn_image_0000002736433551.png)

## 配置权限

Car Kit为开发者提供了两类接口：导航类接口和出行互联类接口，使用对应接口需要分别配置相应的权限。

* 使用导航类接口需要配置ohos.permission.ACCESS\_SERVICE\_NAVIGATION\_INFO权限。
* 使用出行互联类接口需要配置ohos.permission.ACCESS\_CAR\_DISTRIBUTED\_ENGINE权限。

开发者需要在entry/src/main路径下的应用配置文件module.json5中配置所需权限。示例代码如下所示：

```typescript
{
  "module": {
    "requestPermissions": [
      {
        "name": "ohos.permission.ACCESS_CAR_DISTRIBUTED_ENGINE"
      },
      {
        "name": "ohos.permission.ACCESS_SERVICE_NAVIGATION_INFO"
      }
    ]
  }
}
```

## 配置能力

开发者需要在entry/src/main路径下的应用配置文件module.json5的abilities数组中配置导航流转能力或HiCar能力，具体步骤如下：

1. 在[skills](module-configuration-file.md#skills标签)中配置导航信息服务的actions。

   **说明** 

   生态应用如有其它skills配置，请避免直接修改现有的配置，需在skills数组内追加。

   ```typescript
   "skills": [
     {
       "entities": [
         "entity.system.default"
       ],
       "actions": [
         "action.navigation.infoservice"
       ]
     },
     // 其它 skills 配置
     {
       // ...
     }
   ]
   ```
2. 在元数据信息metadata中配置导航流转能力或HiCar能力。具体示例代码如下所示：

   ```typescript
   {
     "module": {
       "abilities": [
        {
           "name": "xxxx",
           "srcEntry": "xxxx",
           "description": "xxxx",
           "skills": [
             {
               "entities": [
                 "entity.system.home"
               ],
               "actions": [
                 "action.system.home"
               ]
             },
             {
               "entities": [
                 "entity.system.default"
               ],
               "actions": [
                 "action.navigation.infoservice"
               ]
             }
           ],
           "metadata": [
             {
               "name" : "carHopCapability",
               "value" : "carHopNavi,getOnCarNavi,insideCarNavi,getOffCarNavi"
             },
             {
               "name" : "hiCarCapability",
               "value" :"basicNavi,shortcutOper,multiScreenUI,mapUIOper,updateNaviStatus,searchPOI"
             }
           ]
         }
       ]
     }
   }
   ```

metadata的name可选值：carHopCapability、hiCarCapability。

* name取值为carHopCapability时，代表适配了导航流转的能力。对应的value值根据不同的业务场景取值如下：

  | value | 场景 |
  | --- | --- |
  | carHopNavi | 碰一碰导航流转，不可与碰一碰地址流转并存。 |
  | carHopAddress | 碰一碰地址流转，不可与碰一碰导航流转并存。 |
  | getOnCarNavi | 上车导航自动流转。 |
  | insideCarNavi | 车内导航自动流转。 |
  | getOffCarNavi | 下车步行导航流转。 |
* name取值为hiCarCapability时，代表适配了HiCar的能力。对应的value值根据不同的业务场景取值如下：

  | value | 场景 |
  | --- | --- |
  | basicNavi | 适配基础导航功能，对应指令：  1. START\_NAVIGATION  2. STOP\_NAVIGATION |
  | shortcutOper | 适配快捷操作功能，对应指令：  1. GO\_HOME  2. GO\_TO\_COMPANY |
  | multiScreenUI | 多屏显示适配功能，对应指令：  1. START\_MAP\_LAYER  2. STOP\_MAP\_LAYER |
  | mapUIOper | 地图UI控制功能，对应指令：  1. ZOOM\_IN\_MAP  2. ZOOM\_OUT\_MAP  3. CHANGE\_THEME |
  | updateNaviStatus | 适配地图状态和地图元数据，对应指令：  1. START\_UPDATE\_NAVIGATION\_STATUS  2. STOP\_UPDATE\_NAVIGATION\_STATUS |
  | searchPOI | 适配地址搜索功能，对应指令：  SEARCH\_POI |

  关于指令的更多详情请查阅[CommandType](../harmonyos-references/car-navigationinfomgr.md#commandtype)。
