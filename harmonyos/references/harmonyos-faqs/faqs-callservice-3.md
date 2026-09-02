---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-callservice-3
title: 当应用主进程被杀死，企业联系人信息来去电页面显示的内容如何获取
breadcrumb: FAQ > 应用服务开发 > VoIP通话服务（Call Service Kit） > 当应用主进程被杀死，企业联系人信息来去电页面显示的内容如何获取
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:47+08:00
doc_updated_at: 2026-08-12
content_hash: sha256:ed8303e5ff10a40c8a5880f4576527534bde90290f80c7989efce9f8559afbaf
---

## 问题现象

通过公共事件订阅的方式，可以在CallerInfoQueryExtensionAbility中获取到企业联系人信息，但是主进程必须存活。如果在不依赖主进程的情况下，Call kit扩展组件如何才能获取到企业联系人信息？

## 背景知识

* [企业联系人信息来去电页面显示能力](../harmonyos-guides/callservice-enterprise-contact-display.md)可以方便用户识别来去电人信息，快速回应，增强企业内部沟通效率。
* 通过自定义组件继承[CallerInfoQueryExtensionAbility](../harmonyos-references/callservicekit-callerinfoquery-extension-ability.md#callerinfoqueryextensionability)，重写[onQueryCallerInfo](../harmonyos-references/callservicekit-callerinfoquery-extension-ability.md#onquerycallerinfo)(phoneNumber: string)：Promise<CallerInfo>方法，在此方法实现根据号码查询企业联系人的业务逻辑，成功获取企业联系人信息后，可通过resolve返回企业联系人信息，获取失败后，可通过reject返回自定义的错误信息。

## 解决方案

1. 通过企业邮箱[申请接入](../harmonyos-guides/callservice-enterprise-contact-display.md#申请接入)企业联系人信息来去电页面显示能力。
2. 参考[通过关系型数据库实现数据持久化 (ArkTS)](../harmonyos-guides/data-persistence-by-rdb-store.md)，主进程创建数据库，创建SQL表，此表含有企业信息必要字段，往表中插入一条数据前，先查询是否已有此条数据，此处需使用await等待查询结束。参考示例代码如下所示：

   ```ts
   import { ConfigurationConstant, UIAbility } from '@kit.AbilityKit';
   import { hilog } from '@kit.PerformanceAnalysisKit';
   import { window } from '@kit.ArkUI';
   import { relationalStore } from '@kit.ArkData';
   import { BusinessError } from '@kit.BasicServicesKit';

   const DOMAIN = 0x0000;

   export default class EntryAbility extends UIAbility {
     isQuery: boolean = false;
     phoneNumber: string = 'xxx';

     // 需手动添加电话号码

     onCreate(): void {
       this.context.getApplicationContext().setColorMode(ConfigurationConstant.ColorMode.COLOR_MODE_NOT_SET);
       hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onCreate');
     }

     onDestroy(): void {
       hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onDestroy');
     }

     async queryData(store: relationalStore.RdbStore): Promise<void> {
       let predicates1 = new relationalStore.RdbPredicates('EMPLOYEE');
       predicates1.equalTo('phoneNumber', this.phoneNumber); // 匹配表'EMPLOYEE'中'phoneNumber'为'xxx'的字段
       let resultSet =
         await store.query(predicates1, ['ID', 'phoneNumber', 'contactName', 'employeeId', 'department', 'position']);
       hilog.info(DOMAIN, 'testTag',
         `ResultSet column names: ${resultSet.columnNames}, column count: ${resultSet.columnCount}`);
       // resultSet是一个数据集合的游标，默认指向第-1个记录，有效的数据从0开始。
       while (resultSet.goToNextRow()) {
         const id = resultSet.getLong(resultSet.getColumnIndex('ID'));
         const phoneNumber = resultSet.getString(resultSet.getColumnIndex('phoneNumber'));
         const contactName = resultSet.getString(resultSet.getColumnIndex('contactName'));
         const employeeId = resultSet.getString(resultSet.getColumnIndex('employeeId'));
         const department = resultSet.getString(resultSet.getColumnIndex('department'));
         const position = resultSet.getString(resultSet.getColumnIndex('position'));
         hilog.info(DOMAIN, 'testTag',
           `id=${id},phoneNumber=${phoneNumber} contactName=${contactName}, employeeId=${employeeId}, department=${department}, position=${position}`);
         this.isQuery = true;
       }
       // 释放数据集的内存
       resultSet.close();
     }

     onWindowStageCreate(windowStage: window.WindowStage): void {
       hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onWindowStageCreate');
       windowStage.loadContent('pages/Index', (err) => {
         if (err.code) {
           hilog.error(DOMAIN, 'testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err));
           return;
         }
         hilog.info(DOMAIN, 'testTag', 'Succeeded in loading the content.');
       });

       const STORE_CONFIG: relationalStore.StoreConfig = {
         name: 'RdbTest.db', // 数据库文件名
         securityLevel: relationalStore.SecurityLevel.S3, // 数据库安全级别
         encrypt: false, // 可选参数，指定数据库是否加密，默认不加密
         customDir: 'customDir/subCustomDir', // 可选参数，数据库自定义路径。数据库将在如下的目录结构中被创建：context.databaseDir+'/rdb/'+customDir，其中context.databaseDir是应用沙箱对应的路径，'/rdb/'表示创建的是关系型数据库，customDir表示自定义的路径。当此参数不填时，默认在本应用沙箱目录下创建RdbStore实例。
         isReadOnly: false // 可选参数，指定数据库是否以只读方式打开。该参数默认为false，表示数据库可读可写。该参数为true时，只允许从数据库读取数据，不允许对数据库进行写操作，否则会返回错误码801。
       };

       const SQL_CREATE_TABLE =
         'CREATE TABLE IF NOT EXISTS EMPLOYEE (ID INTEGER PRIMARY KEY AUTOINCREMENT, phoneNumber TEXT NOT NULL, contactName TEXT NOT NULL, employeeId TEXT NOT NULL, department TEXT NOT NULL, position TEXT NOT NULL)'; // 建表Sql语句

       relationalStore.getRdbStore(this.context, STORE_CONFIG, async (err, store) => {
         if (err) {
           hilog.error(DOMAIN, 'testTag', `Failed to get RdbStore. Code:${err.code}, message:${err.message}`);
           return;
         }
         hilog.info(DOMAIN, 'testTag', 'Succeeded in getting RdbStore.');

         store.executeSql(SQL_CREATE_TABLE).then(() => {
           hilog.info(DOMAIN, 'testTag', 'create employee table success!');
         }).catch((err: BusinessError) => {
           hilog.error(DOMAIN, 'testTag', `Failed to executeSql. Code:${err.code}, message:${err.message}`);
           return;
         }); // 创建数据表，以便后续调用insert接口插入数据

         await this.queryData(store);

         hilog.info(DOMAIN, 'testTag', 'isQuery: %s', String(this.isQuery));
         if (this.isQuery) {
           return;
         }

         const valueBucket1: relationalStore.ValuesBucket = {
           'phoneNumber': this.phoneNumber,
           'contactName': '李四',
           'employeeId': '123456',
           'department': '开发者平台',
           'position': '工程师'
         };
         store.insert('EMPLOYEE', valueBucket1, (err: BusinessError, rowId: number) => {
           if (err) {
             hilog.error(DOMAIN, 'testTag', `Failed to insert data. Code:${err.code}, message:${err.message}`);
             return;
           }
           hilog.info(DOMAIN, 'testTag', `Succeeded in inserting data. rowId:${rowId}`);
         });
       });
     }

     onWindowStageDestroy(): void {
       hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onWindowStageDestroy');
     }

     onForeground(): void {
       hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onForeground');
     }

     onBackground(): void {
       hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onBackground');
     }
   }
   ```

3. Call kit扩展组件继承CallerInfoQueryExtensionAbility，并复写onQueryCallerInfo方法，在此方法中根据电话号码查询对应的关系型数据库，必须使用await等待查询结果后，再进行数据返回，参考示例代码如下所示：

   ```ts
   import { CallerInfoQueryExtensionAbility, CallerInfo } from '@kit.CallServiceKit';
   import { common } from '@kit.AbilityKit';
   import { relationalStore } from '@kit.ArkData';
   import { hilog } from '@kit.PerformanceAnalysisKit';

   const DOMAIN = 0x0000;

   export default class EntryCallerInfoQueryExtAbility extends CallerInfoQueryExtensionAbility {
     isSuccess: boolean = false;
     contactName: string = '';
     employeeId: string = '';
     department: string = '';
     position: string = '';

     async queryData(phoneNumber: string): Promise<void> {
       let context = this.context as common.Context;
       const STORE_CONFIG: relationalStore.StoreConfig = {
         name: 'RdbTest.db', // 数据库文件名
         securityLevel: relationalStore.SecurityLevel.S3, // 数据库安全级别
         encrypt: false, // 可选参数，指定数据库是否加密，默认不加密
         customDir: 'customDir/subCustomDir', // 可选参数，数据库自定义路径。数据库将在如下的目录结构中被创建：context.databaseDir+'/rdb/'+customDir，其中context.databaseDir是应用沙箱对应的路径，'/rdb/'表示创建的是关系型数据库，customDir表示自定义的路径。当此参数不填时，默认在本应用沙箱目录下创建RdbStore实例。
         isReadOnly: false // 可选参数，指定数据库是否以只读方式打开。该参数默认为false，表示数据库可读可写。该参数为true时，只允许从数据库读取数据，不允许对数据库进行写操作，否则会返回错误码801。
       };
       let store = await relationalStore.getRdbStore(context, STORE_CONFIG);
       let predicates1 = new relationalStore.RdbPredicates('EMPLOYEE');
       predicates1.equalTo('phoneNumber', phoneNumber); // 匹配表'EMPLOYEE'中'phoneNumber'为'xxx'的字段
       let resultSet =
         await store.query(predicates1, ['ID', 'phoneNumber', 'contactName', 'employeeId', 'department', 'position']);
       hilog.info(DOMAIN, 'testTag',
         `ResultSet column names: ${resultSet.columnNames}, column count: ${resultSet.columnCount}`);
       // resultSet是一个数据集合的游标，默认指向第-1个记录，有效的数据从0开始。
       while (resultSet.goToNextRow()) {
         const id = resultSet.getLong(resultSet.getColumnIndex('ID'));
         this.contactName = resultSet.getString(resultSet.getColumnIndex('contactName'));
         this.employeeId = resultSet.getString(resultSet.getColumnIndex('employeeId'));
         this.department = resultSet.getString(resultSet.getColumnIndex('department'));
         this.position = resultSet.getString(resultSet.getColumnIndex('position'));
         hilog.info(DOMAIN, 'testTag',
           `id=${id}, contactName=${this.contactName}, employeeId=${this.employeeId}, department=${this.department}, position=${this.position}`);
         this.isSuccess = true;
       }
       // 释放数据集的内存
       resultSet.close();
     }

     async onQueryCallerInfo(phoneNumber: string): Promise<CallerInfo> {
       hilog.info(DOMAIN, 'testTag', 'entry call kit, phoneNumber is %s', phoneNumber);
       try {
         await this.queryData(phoneNumber);
       } catch (error) {
         hilog.error(DOMAIN, 'testTag', `error msg is ${error.message}`);
       }

       hilog.info(DOMAIN, 'testTag', 'isSuccess: %s', String(this.isSuccess));
       return new Promise<CallerInfo>((resolve, reject) => {
         // 在此处实现根据号码查询企业联系人的业务逻辑
         if (this.isSuccess) {
           // 查询成功，返回结果
           resolve({
             contactName: this.contactName,
             employeeId: this.employeeId,
             department: this.department,
             position: this.position
           });
         } else {
           // 查询失败，返回错误原因
           reject({
             code: 10001,
             msg: 'query fail'
           });
         }
       });
     }
   }
   ```
4. 在应用配置文件module.json5中注册extensionAbilities。

   ```json
   "extensionAbilities": [
     {
       "name": "EntryCallerInfoQueryExtAbility",
       "srcEntry": "./ets/EntryCallerInfoQueryExtAbility/EntryCallerInfoQueryExtAbility.ets",
       // EntryCallerInfoQueryExtAbility组件所在文件
       "type": "callerInfoQuery"
     },
     {
       "name": "EntryBackupAbility",
       "srcEntry": "./ets/entrybackupability/EntryBackupAbility.ets",
       "type": "backup",
       "exported": false,
       "metadata": [
         {
           "name": "ohos.extension.backup",
           "resource": "$profile:backup_config"
         }
       ],
     }
   ]
   ```
5. 在调试设备上，前往“电话”，点击右上角的“更多”图标，前往“设置”-“陌生号码和信息识别”，打开对应企业应用的号码识别功能开关，进行调试。

## 常见FAQ

Q：数据库字段以及数据库逻辑可以自定义吗？

A：可以的，只要保证拿出来的内容和需要展示的字段能够匹配上就行。

Q：onQueryCallerInfo方法中可以通过调用网络接口进行查询联系人信息吗？

A：onQueryCallerInfo方法中查询逻辑可以通过调用网络接口进行查询，需要保证网络接口不超时，查询完毕后返回的联系人字段符合规范。

Q：来去电都会自动触发onQueryCallerInfo方法吗？

A：是的，都会自动触发该方法的。

Q：使用该功能，用户必须手动在手机设置-陌生号码和信息识别开关吗？

A：是的，因为涉及到信息采集和一些协议，具体协议内容可以在手机设置-陌生号码和信息识别界面点击查看。

Q：Call Service Kit应用通话过程中切换到后台无法杀死，为什么？

A：目前规格通话过程中应用在后台不能杀死，通话挂断后才能杀死后台，原因是确保通话过程中应用不会被意外关闭导致通话突然中断，规格和运营商通话保持一致。

Q：在CallerInfoQueryExtensionAbility中使用getContext()方法获取上下文失败导致无法获取首选项数据。

A：在CallerInfoQueryExtensionAbility中由于脱离UI页面使用getContext()方法，导致获取上下文不准确，需要使用this.context获取上下文后传递给后续代码使用，避免在工具类中直接使用getContext()方法获取。
