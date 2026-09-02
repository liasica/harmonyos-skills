---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-healthservice-2
title: Health Service Kit授权状态变更后未及时生效如何解决
breadcrumb: FAQ > 应用服务开发 > 运动健康数据服务（Health Service Kit） > Health Service Kit授权状态变更后未及时生效如何解决
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:52+08:00
doc_updated_at: 2026-08-26
content_hash: sha256:6a15d58f2c7934443793f49afbd9f61d20597f547a334564d9a92c121bae757e
---

## 问题现象

* 场景一：应用向用户申请访问健康数据，用来获取当日的步数。当用户完成授权，关闭授权窗口后，发现页面上的步数数据未刷新，仍然显示为0。

  关闭应用后，再次打开，发现数据被刷新。

* 场景二：用户在「设置/运动健康账号授权应用」中取消对应用的授权后，调用[healthStore.getAuthorizations](../harmonyos-references/health-api-healthstore.md#healthstoregetauthorizations)仍返回已取消的授权信息，且healthService.workout.readActivityReport仍能成功执行，授权取消未立即生效。

## 背景知识

* [申请应用权限](../harmonyos-guides/request-app-permissions.md)：应用在访问数据或者执行操作时，需要评估该行为是否需要应用具备相关的权限。
* [向用户申请授权](../harmonyos-guides/request-user-authorization.md)：当应用需要访问用户的隐私信息或使用系统能力时，例如获取位置信息、访问日历、使用相机拍摄照片或录制视频等，应该向用户请求授权，这部分权限是user\_grant权限。
* [healthStore.cancelAuthorizations](../harmonyos-references/health-api-healthstore.md#healthstorecancelauthorizations)：取消运动健康数据服务的所有授权，调用后授权立即生效。
* [healthStore.getAuthorizations](../harmonyos-references/health-api-healthstore.md#healthstoregetauthorizations)：查询已授权的权限信息。

## 问题定位

* 场景一：

  根据HiLog日志进行分析：

  1. 启动应用，在应用申请获取用户授权时，有如下日志信息：

     ```txt
         07-07 18:56:15.228   8333-8546     C0420A/应用包名/WMSLife   应用包名  I     [] GeneratePersistentId(3137): persistentId: 0, persistentId_: 1107873795
         07-07 18:56:15.228   8333-8546     C0420D/应用包名/WMSUiext  应用包名  I     []: persistentId: 1107873795, bundleName: com.huawei.hmos.security.privacycenter, moduleName: , abilityName: PermissionGrantAbility
         07-07 18:56:15.228   8333-8333     C0392A/应用包名           应用包名  I     [(100000:100000:scope)] [@667][ID: 1] The state is changing from 'NONE' to 'FOREGROUND'.
     ```

     这里说明已经获取到了用户的授权，但是之后的日志没有发现有获取相关数据刷新数据的过程。
  2. 对比第二次启动应用，有如下日志信息：

     ```txt
         07-07 17:26:23.845   36285-36373   C05A01/应用包名Permission  应用包名  I     [IsDynamicRequest:453]TokenID: 537454549, bundle: com.huawei.hmos.security.privacycenter, uiExAbility: PermissionGrantAbility, serExAbility: PermissionServiceGrantAbility.
         07-07 17:26:23.845   36285-36373   C05A01/应用包名Permission  应用包名  I     [IsDynamicRequest:457]Permission: ohos.permission.ACTIVITY_MOTION: state: 0
         07-07 17:26:23.845   36285-36373   C05A01/应用包名Permission  应用包名  I     [RequestPermissionsFromUserExecute:688]It does not need to request permission
     ```

     通过上述日志信息分析，说明应用判断当前已经获取到用户的授权。

     接着查看日志：

     ```txt
         07-07 19:41:21.780   25282-25282   A02537/com.hua...nationManager  com.huawe...lth.core  I     subscribeHealthData: cloud sync change!
         07-07 19:41:21.783   25282-25282   A02537/com.hua...leStatService  com.huawe...lth.core  I     readData: timeId: 1751888481783 and request: {"sampleStatDataType":{"id":200009},"startLocalDate":"07/07/2025","endLocalDate":"07/07/2025"}
         07-07 19:41:21.783   25282-25282   A02537/com.hua...leStatService  com.huawe...lth.core  I     readData: timeId: 1751888481783 queryStatData enter
     ```

     通过上述日志分析，应用在判断获取到用户授权后，调用相关接口查询相应的数据并刷新界面上的信息。
* 场景二：

  系统侧的授权信息存在缓存机制，当前缓存时效为2小时。用户在设置页面取消授权后，缓存中的授权状态不会立即清除，导致[healthStore.getAuthorizations](../harmonyos-references/health-api-healthstore.md#healthstoregetauthorizations)返回的是缓存的旧授权状态，healthService.workout.readActivityReport仍能成功执行。

## 分析结论

* 场景一：

  应用在首次获取授权时，当用户授权后没有相应的逻辑处理。
* 场景二：

  授权状态缓存机制导致取消授权不立即生效。系统侧授权信息缓存时效为2小时，在设置页面取消授权后，缓存不会立刻清除。

## 修改建议

* 场景一：

  动态向用户申请授权，是指在应用程序运行时向用户请求授权的过程。可以通过调用requestPermissionsFromUser()方法来实现。该方法接收一个权限列表参数，例如位置、日历、相机、麦克风等。用户可以选择授予权限或者拒绝授权。

  参考如下示例代码：

  ```ts
  import { healthStore } from '@kit.HealthServiceKit';
  import { common } from '@kit.AbilityKit';
  import { hilog } from '@kit.PerformanceAnalysisKit';
  import { healthService } from '@kit.HealthServiceKit';

  export class AuthManagement {
    public static async auth(context: common.UIAbilityContext) {
      try {
        let authorizationParameter: healthStore.AuthorizationRequest = {
          readDataTypes: [healthStore.exerciseSequenceHelper.DATA_TYPE,
            healthStore.samplePointHelper.dailyActivities.DATA_TYPE,
            healthStore.healthSequenceHelper.sleepRecord.DATA_TYPE,
            healthStore.samplePointHelper.bodyTemperature.DATA_TYPE],
          writeDataTypes: [healthStore.exerciseSequenceHelper.DATA_TYPE,
            healthStore.healthSequenceHelper.sleepRecord.DATA_TYPE,
            healthStore.samplePointHelper.bodyTemperature.DATA_TYPE]
        };

        let authorizationResponse: healthStore.AuthorizationResponse =
          await healthStore.requestAuthorizations(context, authorizationParameter);
        let result: string = 'Succeeded in requesting authorization.\n';
        hilog.info(0x0000, 'testTag', 'Succeeded in requesting authorization.');
        authorizationResponse.writeDataTypes.forEach(dataType => {
          result += `grantedWriteDataType is : ${dataType.name}` + '\n';
          hilog.info(0x0000, 'testTag', `grantedWriteDataType is : ${dataType.name}`);
        });
        authorizationResponse.readDataTypes.forEach(dataType => {
          result += `grantedReadDataTypes is : ${dataType.name}` + '\n';
          hilog.info(0x0000, 'testTag', `grantedReadDataTypes is : ${dataType.name}`);
        });

        return result;
      } catch (err) {
        hilog.error(0x0000, 'testTag', `Failed to request authorization. Code: ${err.code}, message: ${err.message}`);
        return `Failed to request authorization. Code: ${err.code}, message: ${err.message}`;
      }
    }

    public static async getAuth(): Promise<string> {
      try {
        let parameter: healthStore.AuthorizationRequest = {
          readDataTypes: [healthStore.exerciseSequenceHelper.DATA_TYPE,
            healthStore.samplePointHelper.dailyActivities.DATA_TYPE,
            healthStore.healthSequenceHelper.sleepRecord.DATA_TYPE,
            healthStore.samplePointHelper.bodyTemperature.DATA_TYPE],
          writeDataTypes: [healthStore.exerciseSequenceHelper.DATA_TYPE,
            healthStore.healthSequenceHelper.sleepRecord.DATA_TYPE,
            healthStore.samplePointHelper.bodyTemperature.DATA_TYPE]
        };

        let queryAuthorizationResponse = await healthStore.getAuthorizations(parameter);
        hilog.info(0x0000, 'testTag', 'Succeeded in getting authorization.');
        let result: string = 'Succeeded in getting authorization.\n';
        queryAuthorizationResponse.writeDataTypes.forEach(dataType => {
          hilog.info(0x0000, 'testTag', `grantedWriteDataType is : ${dataType.name}`);
          result += `grantedWriteDataType is : ${dataType.name}` + '\n';
        });
        queryAuthorizationResponse.readDataTypes.forEach(dataType => {
          hilog.info(0x0000, 'testTag', `grantedReadDataTypes is : ${dataType.name}`);
          result += `grantedReadDataTypes is : ${dataType.name}` + '\n';
        });
        return result;
      } catch (err) {
        hilog.error(0x0000, 'testTag', `Failed to get authorization. Code: ${err.code}, message: ${err.message}`);
        return `Failed to get authorization. Code: ${err.code}, message: ${err.message}`;
      }
    }

    public static async cancelAuthAll(): Promise<string> {
      try {
        await healthStore.cancelAuthorizations();
        hilog.info(0x0000, 'testTag', 'Succeeded in cancelling authorization.');
        return 'Succeeded in cancelling authorization.';
      } catch (err) {
        hilog.error(0x0000, 'testTag', `Failed to cancel authorization. Code: ${err.code}, message: ${err.message}`);
        return `Failed to cancel authorization. Code: ${err.code}, message: ${err.message}`;
      }
    }
  }

  export class WorkoutManagement {
    public static async readActivityReport(): Promise<string> {
      try {
        let activityReport: healthService.workout.ActivityReport = await healthService.workout.readActivityReport();
        hilog.info(0x0000, 'testTag', 'Succeeded in reading ActivityReport');
        let result = 'Succeeded in reading ActivityReport\n';
        Object.keys(activityReport).forEach(key => {
          result += `the ${key} is ${activityReport[key]}` + '\n';
          hilog.info(0x0000, 'testTag', `the ${key} is ${activityReport[key]}`);
        });
        return result;
      } catch (err) {
        hilog.error(0x0000, 'testTag', `Failed to read ActivityReport. Code: ${err.code}, message: ${err.message}`);
        return `Failed to read ActivityReport. Code: ${err.code}, message: ${err.message}`;
      }
    }
  }

  @Entry
  @Component
  struct WorkoutIndex {
    @State log: string = '';

    build() {
      Column() {
        Text('授权管理').fontWeight(FontWeight.Bold).fontSize(30).height('20%');

        Row() {
          Button('授权').width('50%').onClick(async () => {
            this.log = await AuthManagement.auth(this.getUIContext().getHostContext() as common.UIAbilityContext);
          });
        }.height('10%').alignItems(VerticalAlign.Top);

        Row() {
          Button('取消授权').width('50%').onClick(async () => {
            this.log = await AuthManagement.cancelAuthAll();
          });
        }.height('10%').alignItems(VerticalAlign.Top);

        Row() {
          Button('查询权限').width('50%').onClick(async () => {
            this.log = await AuthManagement.getAuth();
          });
        }.height('10%').alignItems(VerticalAlign.Top);

        Text('运动联动').fontWeight(FontWeight.Bold).fontSize(30).height('20%');

        Row() {
          Button('读取实时三环数据').width('50%').onClick(async () => {
            this.log = await WorkoutManagement.readActivityReport();
          });
        }.height('10%').alignItems(VerticalAlign.Top);

        Column() {
          Column() {
            Text('日志打印：').fontSize(15).textAlign(TextAlign.Start).fontWeight(FontWeight.Bold);
          }.alignItems(HorizontalAlign.Start).width('90%');

          Column() {
            Text(this.log).fontSize(10).textAlign(TextAlign.Start);
          }.alignItems(HorizontalAlign.Start).width('90%');
        }.alignItems(HorizontalAlign.Start)
      }.alignItems(HorizontalAlign.Center).height('100%').width('100%')
      .justifyContent(FlexAlign.Start)
    }
  }
  ```
* 场景二：

  用户在「设置/运动健康账号授权应用」中取消对本应用的授权后，系统侧的授权信息存在缓存机制，当前缓存时效为2小时，不会立刻被清除。因此，授权取消不会立即生效，需等待缓存过期后系统才会更新授权状态。
