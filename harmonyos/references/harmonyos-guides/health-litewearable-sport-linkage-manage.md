---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/health-litewearable-sport-linkage-manage
title: 运动联动管理
breadcrumb: 指南 > 应用服务 > Health Service Kit（运动健康服务） > 开发接入 > LiteWearable应用开发 > 运动联动管理
category: harmonyos-guides
scraped_at: 2026-09-05T06:15:08+08:00
doc_updated_at: 2026-09-04
content_hash: sha256:207178477a99fa7e18a4db8afff1db9a19f0eec226c22cc257ec312cb1c5e98a
---

## 场景介绍

从6.1.1(24) 版本开始，支持运动联动管理。

运动联动管理包含运动联动的配置、开启、暂停、恢复、停止，数据订阅、取消订阅和下发融合数据，以及锻炼记录的读写。

## 接口说明

| 接口名 | 描述 |
| --- | --- |
| [config](../harmonyos-references/health-api-healthservice-lite.md#workoutconfig)(workoutConfig: WorkoutConfig): void | 运动联动配置。 |
| [start](../harmonyos-references/health-api-healthservice-lite.md#workoutstart)(): StartResult | 开启运动联动。 |
| [pause](../harmonyos-references/health-api-healthservice-lite.md#workoutpause)(): void | 暂停运动联动。 |
| [resume](../harmonyos-references/health-api-healthservice-lite.md#workoutresume)(): void | 恢复运动联动。 |
| [stop](../harmonyos-references/health-api-healthservice-lite.md#workoutstop)(): void | 停止运动联动。 |
| [onData](../harmonyos-references/health-api-healthservice-lite.md#workoutondata)(dataType: undefined, listener: Callback<[SampleReal](../harmonyos-references/health-api-healthservice-lite.md#samplereal)[]>): void | 订阅所有类型的数据。 |
| [offData](../harmonyos-references/health-api-healthservice-lite.md#workoutoffdata)(dataType: undefined, listener?: Callback<[SampleReal](../harmonyos-references/health-api-healthservice-lite.md#samplereal)[]>): void | 取消订阅所有类型的数据。 |
| [sendData](../harmonyos-references/health-api-healthservice-lite.md#workoutsenddata)(sampleReal: [SampleReal](../harmonyos-references/health-api-healthservice-lite.md#samplereal)[]): void | 下发融合数据。 |
| [readData](../harmonyos-references/health-api-healthstore-lite.md#healthstorereaddata)<T extends ExerciseSequence>(request: exercisesequencereadrequest, callback: Callback<T[]>): void | 读取最新一条锻炼记录。 |
| [saveData](../harmonyos-references/health-api-healthstore-lite.md#healthstoresavedata)(exerciseSequence: ExerciseSequence): void | 保存锻炼记录。 |

## 开发前检查

* 完成[申请运动健康服务](health-apply.md)。
* 需先通过[用户授权](health-litewearable-add-permissions.md)接口引导用户授权，用户授权应根据[权限说明](health-permission-description.md#lite-wearable)中要求来打开锻炼记录读/写和联动接口控制权限。
* 常见问题请参考[Health Service Kit常见问题](health-faqs.md)。

## 开发步骤

1. 导入运动健康服务功能模块。

   ```javascript
   import healthService from '@hms.health.service';
   import healthStore from '@hms.health.store';
   ```
2. 配置联动。

   ```javascript
   function config() {
     let workoutOptions = {
       linkageType: healthService.workout.LinkageType.ACTIVITY_LINK,
       sportType: healthStore.exerciseSequenceHelper.badminton.EXERCISE_TYPE.id,
       activityGoals: [
         {
           type: healthService.workout.TargetType.CALORIE,
           value: 100
         }
       ]
     };
     try {
       healthService.workout.config(workoutOptions);
     } catch (err) {
       // 异常场景处理
     }
   }
   ```
3. 开启联动。

   ```javascript
   function start() {
     try {
       let startResult = healthService.workout.start();
     } catch (err) {
       // 异常场景处理
     }
   }
   ```
4. 暂停/恢复联动。

   ```javascript
   function pause() { // 暂停联动
     try {
       healthService.workout.pause();
     } catch (err) {
       // 异常场景处理
     }
   }

   function resume() { // 恢复联动
     try {
       healthService.workout.resume();
     } catch (err) {
       // 异常场景处理
     }
   }
   ```
5. 订阅数据，可以实时获取运动数据，并对获取的运动数据进行处理。

   ```javascript
   function onData() {
     const callback = (sampleReals) => {
       // 运动数据回调处理流程
     };

     try {
       healthService.workout.onData(undefined, callback);
     } catch (e) {
       if (e.code === 1009104001) { // 联动已开启其他应用已调用start开启联 动
         // 回到准备界面
       } else if (e.code === 1009104003) { // 在当前状态下，指令非法。请先 开启运动联动
         // 回到准备界面
       }
     }
   }
   ```
6. 下发融合数据（根据需求调整调用时机）。

   ```javascript
   function sendData() {
     let sampleReal = {
       dataType: healthStore.healthDataTypes.WORKOUT_REALTIME,
       time: new Date().getTime(),
       fields: {
         avgShotSpeed: 10
       }
     };

     try {
       healthService.workout.sendData([sampleReal]);
     } catch(err) {
      // 异常场景处理
     }
   }
   ```
7. 解订阅数据（根据需求调整调用时机）。

   ```javascript
   function offData() {
     const callback = (sampleReals) => {
       // 运动数据回调处理流程
     };

     try {
       healthService.workout.offData(undefined, callback);
     } catch (e) {
       // 异常场景处理
     }
   }
   ```
8. 保存锻炼记录。

   ```javascript
   function saveData() {
     let healthSequence = {
       dataType: healthStore.healthDataTypes.WORKOUT_REALTIME,
       // insertDataSource插入数据源接口返回的DataSourceId
       dataSourceId: 'xxx',
       localDate: '09/26/2023',
       startTime: 1695740400000,  // 2023-9-26 23:00:00
       endTime: 1695769200000,   // 2023-9-27 07:00:00
       timeZone: '+0800',
       modifiedTime: 1695769200000,
       exerciseType: healthStore.exerciseSequenceHelper.badminton. EXERCISE_TYPE,
       duration: 1800000,
       summaries: {
         avgShotSpeed: 25.5,
         maxShotSpeed: 32.8,
         shots: 125,
         maxContinuousRally: 7,
         forehandStroke: 45,
         backhandStroke: 32,
         overhandStroke: 18,
         underhandStroke: 10,
         smash: 23,
         highClear: 15
       }
     }

     try {
       healthStore.saveData(healthSequence);
     } catch (err) {
       // 异常处理流程
     }
   }
   ```
9. 读取锻炼记录。

   ```javascript
   function readData() {
     const startTime = 1698040800000; // 2023-10-23 14:00:00
     const endTime = 1698042600000; // 2023-10-23 14:30:00

     const sequenceReadRequest = {
       startTime: startTime,
       endTime: endTime,
       exerciseType: healthStore.exerciseSequenceHelper.badminton. EXERCISE_TYPE,
       count: 1,
       sortOrder: healthStore.SortOrder.DESC,
       readOptions: {
         withPartialDetails: ['exerciseHeartRate']
       }
     };

     const callback = (samplePoints) => {
       // 锻炼记录数据回调处理流程
     };

     try {
       healthStore.readData(sequenceReadRequest, callback);
     } catch (err) {
       // 异常处理流程
     }
   }
   ```
10. 停止联动。

    ```javascript
    function stop() {
      try {
        healthService.workout.stop();
      } catch (err) {
        // 异常场景处理
      }
    }
    ```
