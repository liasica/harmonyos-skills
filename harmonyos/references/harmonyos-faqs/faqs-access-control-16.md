---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-access-control-16
title: 应用权限管理界面的权限跳转到系统设置界面，无对应权限
breadcrumb: FAQ > 系统开发 > 安全 > 程序访问控制 > 应用权限管理界面的权限跳转到系统设置界面，无对应权限
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:34+08:00
doc_updated_at: 2026-07-30
content_hash: sha256:1c0720171a7ba3dd0530aa2bb76385ab707209f105ad16729874371a82620028
---

## 问题现象

打开应用设置里的权限管理界面，点击未开启的权限，跳转到系统的应用权限设置界面，无对应权限选项。

## 背景知识

[向用户申请授权](../harmonyos-guides/request-user-authorization.md)：当应用需要访问用户的隐私信息或使用系统能力时，例如获取位置信息、访问日历、使用相机拍摄照片或录制视频等，应该向用户请求授权，用户可以在动态授予权限后通过系统设置来取消应用的权限。

在API23之前，对于授权方式为用户授权的权限，系统设置-应用权限设置页不存在权限是因为应用的权限设置中只展示应用申请过的权限，该特性是系统规格，只有在调用requestPermissionsFromUser这个接口，并且用户选择是否授予权限之后，才会在应用详情页显示该权限开关。从API23开始，系统设置-应用权限设置页会展示所有权限。

## 问题定位

1. 排查在module.json5配置文件的requestPermissions标签中是否声明权限。
2. 根据关键词“requestPermissionsFromUser”过滤日志，发现无相关日志信息。
3. 根据问题现象是直接跳转到应用隐私设置权限页面下无相应权限和系统设计，未申请过的权限不会显示在系统隐私权限设置页面中，说明应用暂未申请过此权限。

## 分析结论

在API23之前，应用在权限管理界面的操作，未先进行相关权限申请，则根据系统设计，无法在系统隐私设置权限页面设置。

## 修改建议

1. 通过[getSelfPermissionStatus](../harmonyos-references/js-apis-abilityaccessctrl.md#getselfpermissionstatus20)接口查询应用权限状态。参考代码：

   ```ts
   getPermissionStatus(permissions: Permissions) {
     try {
       let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
       let data: abilityAccessCtrl.PermissionStatus = atManager.getSelfPermissionStatus(permissions);
       console.info(`data->${data}`);
     } catch (err) {
       console.error(`catch err->${err}`);
     }
   }
   ```
2. 当结果为NOT\_DETERMINED时，表示未操作。应用声明用户授权权限，暂未调用[requestPermissionsFromUser](../harmonyos-references/js-apis-abilityaccessctrl.md#requestpermissionsfromuser9)接口请求用户授权，或用户在设置中将权限状态修改为每次询问，此时可以调用请求用户授权接口进行授权，参考代码：

   ```ts
   reqPermissionFromUser(permissionList: Array<Permissions>) {
     let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
     let context: Context = this.getUIContext().getHostContext() as common.UIAbilityContext;
     atManager.requestPermissionsFromUser(context, permissionList,
       (err: BusinessError, data: PermissionRequestResult) => {
         if (err) {
           console.error(`requestPermissionsFromUser fail, err->${err}`);
         } else {
           console.info(`data permissions: ${data.permissions}`);
           console.info(`data authResults: ${data.authResults}`);
         }
       });
   }
   ```

3. 当前结果为已授权或未授权时，有以下两种方案可以申请授权。
   * 方案一：跳转到系统权限设置页面调整。参考代码：

     ```ts
     applyPermissionsOnStartAbility() {
       let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
       context?.startAbility({
         bundleName: 'com.huawei.hmos.settings',
         abilityName: 'com.huawei.hmos.settings.MainAbility',
         uri: 'application_info_entry', // uri为空的时候，拉起设置主页面
         parameters: {
           pushParams: 'com.example.xxx' // 传要跳转的对应应用的包名
         }
       });
     }
     ```

     效果图如下：

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/HmsZFMVRRaiT6abKLvVBcQ/zh-cn_image_0000002680157833.png "点击放大")
   * 方案二：使用[requestPermissionOnSetting](../harmonyos-references/js-apis-abilityaccessctrl.md#requestpermissiononsetting12)拉起权限设置弹框。参考代码：

     ```ts
     applyPermissionsOnSetting(permissionList: Array<Permissions>) {
       let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
       let context: Context = this.getUIContext().getHostContext() as common.UIAbilityContext;
       atManager.requestPermissionOnSetting(context, permissionList)
         .then((data: Array<abilityAccessCtrl.GrantStatus>) => {
           console.info(`data: ${data}`);
         })
         .catch((err: BusinessError) => {
           console.error(`data: ${err}`);
         });
     }
     ```

     效果图如下：

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c8/v3/830eThRsSyOL6BXrJVAAYg/zh-cn_image_0000002650238254.png "点击放大")

完整代码如下：

```ts
import { abilityAccessCtrl, common, PermissionRequestResult, Permissions } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  build() {
    Column() {
      Button('查询授权状态').onClick(() => {
        this.getPermissionStatus('ohos.permission.CAMERA');
      });
      Button('首次申请授权').onClick(() => {
        this.reqPermissionFromUser(['ohos.permission.CAMERA']);
      });
      Button('非首次申请方式一').onClick(() => {
        this.applyPermissionsOnStartAbility();
      });
      Button('非首次申请授权方式二').onClick(() => {
        this.applyPermissionsOnSetting(['ohos.permission.CAMERA']);
      });
    }
    .height('100%')
    .width('100%');
  }

  getPermissionStatus(permissions: Permissions) {
    try {
      let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
      let data: abilityAccessCtrl.PermissionStatus = atManager.getSelfPermissionStatus(permissions);
      console.info(`data->${data}`);
    } catch (err) {
      console.error(`catch err->${err}`);
    }
  }

  reqPermissionFromUser(permissionList: Array<Permissions>) {
    let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
    let context: Context = this.getUIContext().getHostContext() as common.UIAbilityContext;
    atManager.requestPermissionsFromUser(context, permissionList,
      (err: BusinessError, data: PermissionRequestResult) => {
        if (err) {
          console.error(`requestPermissionsFromUser fail, err->${err}`);
        } else {
          console.info(`data permissions: ${data.permissions}`);
          console.info(`data authResults: ${data.authResults}`);
        }
      });
  }

  applyPermissionsOnStartAbility() {
    let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
    context?.startAbility({
      bundleName: 'com.huawei.hmos.settings',
      abilityName: 'com.huawei.hmos.settings.MainAbility',
      uri: 'application_info_entry', // uri为空的时候，拉起设置主页面
      parameters: {
        pushParams: 'com.example.xxx' // 传要跳转的对应应用的包名
      }
    });
  }

  applyPermissionsOnSetting(permissionList: Array<Permissions>) {
    let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
    let context: Context = this.getUIContext().getHostContext() as common.UIAbilityContext;
    atManager.requestPermissionOnSetting(context, permissionList)
      .then((data: Array<abilityAccessCtrl.GrantStatus>) => {
        console.info(`data: ${data}`);
      })
      .catch((err: BusinessError) => {
        console.error(`data: ${err}`);
      });
  }

}
```
