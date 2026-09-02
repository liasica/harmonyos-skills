---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-local-database-management-65
title: 如何在服务卡片与主应用之间共享持久化数据
breadcrumb: FAQ > 应用框架开发 > 本地数据和文件 > 本地数据库管理 > 如何在服务卡片与主应用之间共享持久化数据
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:29+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:23e00d6358d930c52f37ec553e8670878e84c7cc03144d9356b7cc4f10177a46
---

## 问题现象

在主应用和卡片中需要分别持久化存储数据，如何在服务卡片与主应用之间共享这些数据？

## 背景知识

* [Form Kit（卡片开发服务）](../harmonyos-guides/formkit-overview.md)提供了一种在桌面、锁屏等系统应用上嵌入显示应用信息的开发框架和API，可以将应用内用户关注的重要信息或常用操作抽取到服务卡片（简称“卡片”）上，通过将卡片添加到桌面、锁屏等系统应用上，以达到信息展示、服务直达的便捷体验效果。
* [用户首选项(Preferences)](../harmonyos-guides/data-persistence-by-preferences.md)为应用提供Key-Value键值型的数据处理能力，支持应用持久化轻量级数据，并对其修改和查询。当用户有轻量级的键值型数据需要存储时，可以采用Preferences来进行存储。
* [关系型数据库](../harmonyos-guides/data-persistence-by-rdb-store.md)基于SQLite组件，适用于存储包含复杂关系数据的场景，比如一个班级的学生信息，需要包括姓名、学号、各科成绩等，又或者公司的雇员信息，需要包括姓名、工号、职位等，由于数据之间有较强的对应关系，复杂程度比键值型数据更高，此时需要使用关系型数据库来持久化保存数据。

## 解决方案

* **解决方案一**：在服务卡片与主应用之间使用用户首选项共享持久化数据。
  1. [创建动态卡片](../harmonyos-guides/arkts-ui-widget-creation.md)。
  2. 创建用户首选项操作类PreferencesHelper，该类旨在封装用户首选项（Preferences）的核心操作。为确保全局唯一性，类中定义了静态方法getInstance，以对外提供单一的PreferencesHelper实例。需要注意的是，在getPreferences函数被调用时，应先调用removePreferencesFromCacheSync方法。此操作能够主动清除已缓存的实例，强制系统从持久化文件中重新加载数据，从而保证在多线程并发访问场景下，每次获取的都是最新的首选项数据。

     ```ts
     import { preferences } from '@kit.ArkData';

     export class PreferencesHelper {
       private static instance: PreferencesHelper | null = null;

       public static getInstance() {
         if (PreferencesHelper.instance === null) {
           PreferencesHelper.instance = new PreferencesHelper();
         }
         return PreferencesHelper.instance;
       }

       getPreferences(context: Context, preferencesName: string): preferences.Preferences | undefined {
         try {
           preferences.removePreferencesFromCacheSync(context, preferencesName);
           return preferences.getPreferencesSync(context, { name: preferencesName });
         } catch (error) {
           let err = error as BusinessError;
           console.error(`getPreferences failed, error code=${err.code}, message=${err.message}`);
           return undefined;
         }
       }

       public get(preferences: preferences.Preferences | undefined, key: string, defaultValue: preferences.ValueType) {
         if (preferences === null || preferences === undefined) {
           return;
         }
         return preferences.getSync(key, defaultValue);
       }

       put(preferences: preferences.Preferences | undefined, key: string, defaultValue: preferences.ValueType) {
         if (preferences === null || preferences === undefined) {
           return;
         }
         preferences.putSync(key, defaultValue);
         preferences.flushSync();
       }

       clear() {
         PreferencesHelper.instance = null;
       }
     }
     ```
  3. 在应用主页面中，定义刷新和修改操作，从首选项获取并同步最新数据。

     ```ts
     import { PreferencesHelper } from '../utils/PreferencesHelper';

     @Entry
     @Component
     struct Index {
       @State curNum: number = 0;
       private readonly keyStr: string = 'restNum';

       build() {
         Column({ space: 15 }) {
           Text(`当前用户首选项中数据为：${this.curNum}`);
           Button('刷新数据').onClick(() => {
             // 查询最新的数据
             this.operate(0);
           })
             .width(200);
           Row() {
             Button('减少')
               .onClick(() => {
                 this.operate(-1);
               });
             Button('增加')
               .onClick(() => {
                 this.operate(1);
               });
           }.width(200).justifyContent(FlexAlign.SpaceBetween);
         }
         .padding(16)
         .height('100%')
         .width('100%');
       }

       // 操作首选项
       operate(value: number) {
         let utilHelper = PreferencesHelper.getInstance();
         let myPreferences =
           utilHelper.getPreferences(this.getUIContext()?.getHostContext()?.getApplicationContext()!, this.keyStr);
         let preNum = utilHelper.get(myPreferences, this.keyStr, 0) as number;
         this.curNum = preNum + value;
         if (value == 0) {
           return;
         }
         utilHelper.put(myPreferences, this.keyStr, this.curNum);
       }
     }
     ```
  4. 编写卡片EntryFormAbility生命周期文件。定义operate函数实现卡片端对首选项的操作，分别在onAddForm、onUpdateForm及onFormEvent中调用该操作。

     ```ts
     import { formBindingData, FormExtensionAbility, formInfo, formProvider } from '@kit.FormKit';
     import { PreferencesHelper } from '../utils/PreferencesHelper';

     export default class EntryFormAbility extends FormExtensionAbility {
       private readonly keyStr: string = 'restNum';

       operate(value: number) {
         let utilHelper = PreferencesHelper.getInstance();
         let myPreferences = utilHelper.getPreferences(this.context.getApplicationContext(), this.keyStr);
         let preNum = utilHelper.get(myPreferences, this.keyStr, 0) as number;
         let curNum = preNum + value;
         if (value == 0) {
           return curNum;
         }
         utilHelper.put(myPreferences, this.keyStr, curNum);
         return curNum;
       }

       onAddForm() {
         // Called to return a FormBindingData object.
         // 取值
         let curNum = this.operate(0);
         // 传递至卡片页面
         return formBindingData.createFormBindingData({
           curNum: curNum
         });
       }

       onUpdateForm(formId: string) {
         // 也可取最新数据传递给卡片页面，用于定时/定点刷新等
         let curNum = this.operate(0);
         // 更新
         formProvider.updateForm(formId, formBindingData.createFormBindingData({
           curNum: curNum
         }));
       }

       onFormEvent(formId: string, message: string) {
         console.info('--onFormEvent--', formId, message);
         // 计算
         let preNum: number = JSON.parse(message)['curNum'];
         let curNum = this.operate(preNum);
         // 更新
         formProvider.updateForm(formId, formBindingData.createFormBindingData({
           curNum: curNum
         }));
       }

       onAcquireFormState() {
         // Called to return a {@link FormState} object.
         return formInfo.FormState.READY;
       }
     };
     ```
  5. 在卡片页面中，创建刷新和修改按钮，使用postCardAction发起修改操作。

     ```ts
     @Entry
     @Component
     struct WidgetCard {
       @LocalStorageProp('curNum') curNum: number = 0;

       operate(curNum: number) {
         postCardAction(this, {
           action: 'message',
           abilityName: 'EntryAbility',
           params: {
             curNum: curNum
           }
         });
       }

       build() {
         Column({ space: 15 }) {
           Text(`当前用户首选项中数据为：${this.curNum}`);
           Button('刷新数据').onClick(() => {
             this.operate(0);
           })
             .width(200);
           Row() {
             Button('减少')
               .onClick(() => {
                 this.operate(-1);
               });
             Button('增加')
               .onClick(() => {
                 this.operate(1);
               });
           }.width(200).justifyContent(FlexAlign.SpaceBetween);

         }
         .padding(16)
         .height('100%')
         .width('100%');
       }
     }
     ```
* **解决方案二**：在服务卡片与主应用之间使用关系型数据库共享持久化数据。
  1. [创建动态卡片](../harmonyos-guides/arkts-ui-widget-creation.md)。
  2. 创建关系型数据库的工具类RdbUtils，定义获取数据库连接、对数据库的增、删、改、查操作。接着定义Person实体类，将其作为关系型数据库操作的实体。最后，定义PersonRdbHelper类实现对Person对象在关系型数据库的操作。

     utils/RdbUtils.ets为：

     ```ts
     import { relationalStore } from '@kit.ArkData';
     import { BusinessError } from '@kit.BasicServicesKit';

     const TAG = 'RdbUtils';

     const STORE_CONFIG: relationalStore.StoreConfig = {
       name: 'database.db',
       securityLevel: relationalStore.SecurityLevel.S1,
     };

     export class RdbUtils {
       private rdbStore?: relationalStore.RdbStore;
       private tableName: string = '';
       private sqlCreateTable: string = '';
       private context: Context;

       constructor(context: Context, tableName: string, sqlCreateTable: string) {
         this.context = context;
         this.tableName = tableName;
         this.sqlCreateTable = sqlCreateTable;
       }

       public getRdbStore(): Promise<relationalStore.RdbStore> {
         console.info(TAG, `getRdbStore The rdbStore context: ${this.context}`);
         return new Promise<relationalStore.RdbStore>((resolve, reject) => {
           if (this.rdbStore) {
             console.info(TAG, 'getRdbStore The rdbStore exists.');
             resolve(this.rdbStore);
           }
           relationalStore
             .getRdbStore(this.context, STORE_CONFIG)
             .then((rdbStore: relationalStore.RdbStore) => {
               console.info(TAG, 'getRdbStore successfully.');
               this.rdbStore = rdbStore;
               this.rdbStore.executeSync(this.sqlCreateTable);
               resolve(rdbStore);
             })
             .catch((err: BusinessError) => {
               console.error(TAG, `getRdbStore failed, code is ${err.code},message is ${err.message}`);
               reject(err);
             });
         });
       }

       async insertData(valuesBucket: relationalStore.ValuesBucket): Promise<number> {
         console.info(TAG, `insertData valuesBucket : ${JSON.stringify(valuesBucket)}`);
         let rdbStore = await this.getRdbStore();
         return new Promise<number>((resolve, reject) => {
           rdbStore
             .insert(this.tableName, valuesBucket)
             .then((rowId: number) => {
               console.info(TAG, `insertData successfully. rowId: ${rowId}`);
               resolve(rowId);
             })
             .catch((err: BusinessError) => {
               console.error(TAG, `insertData failed, code is ${err.code},message is ${err.message}`);
               reject(err);
             });
         });
       }

       async batchInsert(valueBucketArray: Array<relationalStore.ValuesBucket>): Promise<number> {
         console.info(TAG, `batchInsert valuesBucket : ${JSON.stringify(valueBucketArray)}`);
         let rdbStore = await this.getRdbStore();
         return new Promise<number>((resolve, reject) => {
           rdbStore
             .batchInsert(this.tableName, valueBucketArray)
             .then((rowId: number) => {
               console.info(TAG, `batchInsert successfully. rowId: ${rowId}`);
               resolve(rowId);
             })
             .catch((err: BusinessError) => {
               console.error(TAG, `batchInsert failed, code is ${err.code},message is ${err.message}`);
               reject(err);
             });
         });
       }

       async deleteData(predicates: relationalStore.RdbPredicates): Promise<number> {
         let rdbStore = await this.getRdbStore();
         return new Promise<number>((resolve, reject) => {
           rdbStore
             .delete(predicates)
             .then((rows: number) => {
               console.info(TAG, `deleteData successfully. rows: ${rows}`);
               resolve(rows);
             })
             .catch((err: BusinessError) => {
               console.error(TAG, `deleteData failed, code is ${err.code},message is ${err.message}`);
               reject(err);
             });
         });
       }

       async updateData(predicates: relationalStore.RdbPredicates, data: relationalStore.ValuesBucket): Promise<number> {
         let rdbStore = await this.getRdbStore();
         return new Promise<number>((resolve, reject) => {
           rdbStore
             .update(data, predicates)
             .then((rows: number) => {
               console.info(TAG, `updateData successfully. rows: ${rows}`);
               resolve(rows);
             })
             .catch((err: BusinessError) => {
               console.error(TAG, `updateData failed, code is ${err.code},message is ${err.message}`);
               reject(err);
             });
         });
       }

       async query(predicates: relationalStore.RdbPredicates): Promise<relationalStore.ResultSet> {
         let rdbStore = await this.getRdbStore();
         return new Promise<relationalStore.ResultSet>((resolve, reject) => {
           rdbStore
             .query(predicates)
             .then((resultSet: relationalStore.ResultSet) => {
               console.info(TAG, `query successfully. rowCount: ${resultSet.rowCount}`);
               resolve(resultSet);
             })
             .catch((err: BusinessError) => {
               console.error(TAG, `query failed, code is ${err.code},message is ${err.message}`);
               reject(err);
             });
         });
       }
     }
     ```

     viewmodel/Person.ets为：

     ```ts
     export class Person {
       pId: string = '';
       pName: string = '';
       pAge: number = 0;
     }
     ```

     utils/FormRdbHelper.ets为：

     ```ts
     import { relationalStore } from '@kit.ArkData';
     import { Person } from '../viewmodel/Person';
     import { RdbUtils } from './RdbUtils';

     const TAG = 'PersonRdbHelper';

     const SQL_CREATE_TABLE: string =
       'CREATE TABLE IF NOT EXISTS PersonTable(pId STRING PRIMARY KEY, pName STRING, pAge NUMBER)';

     const TABLE_NAME = 'PersonTable';
     let rdbUtils: RdbUtils;

     export class PersonRdbHelper {
       private static instance: PersonRdbHelper;

       private constructor(context: Context) {
         console.info(TAG, `constructor Context: ${context}`);
         rdbUtils = new RdbUtils(context, TABLE_NAME, SQL_CREATE_TABLE);
       }

       public static getInstance(context: Context): PersonRdbHelper {
         if (!PersonRdbHelper.instance) {
           PersonRdbHelper.instance = new PersonRdbHelper(context);
         }
         return PersonRdbHelper.instance;
       }

       public insertPerson(person: Person): Promise<number> {
         console.info(TAG, `insertPerson person: ${JSON.stringify(person)}`);
         let valueBucket = this.generateBucket(person);
         return rdbUtils.insertData(valueBucket);
       }

       public deletePerson(pId: string): Promise<number> {
         console.info(TAG, `deletePerson pId: ${pId}`);
         let predicates = new relationalStore.RdbPredicates(TABLE_NAME);
         predicates.equalTo('pId', pId);
         return rdbUtils.deleteData(predicates);
       }

       public updatePerson(person: Person): Promise<number> {
         console.info(TAG, `updatePerson pId: ${person.pId}`);
         let valueBucket = this.generateBucket(person);
         let predicates = new relationalStore.RdbPredicates(TABLE_NAME);
         predicates.equalTo('pId', person.pId);
         return rdbUtils.updateData(predicates, valueBucket);
       }

       public queryAllPerson(): Promise<Array<Person>> {
         console.info(TAG, 'queryAllPerson');
         let predicates = new relationalStore.RdbPredicates(TABLE_NAME);
         return this.queryPerson(predicates);
       }

       public queryPersonByName(formName: string): Promise<Array<Person>> {
         console.info(TAG, 'queryAllPerson');
         let predicates = new relationalStore.RdbPredicates(TABLE_NAME);
         predicates.contains('formName', formName);
         return this.queryPerson(predicates);
       }

       public queryPersonById(pId: string): Promise<Person> {
         console.info(TAG, `queryPersonById pId: ${pId}`);
         let predicates = new relationalStore.RdbPredicates(TABLE_NAME);
         predicates.equalTo('pId', pId);
         return new Promise<Person>(async (resolve) => {
           let personList = await this.queryPerson(predicates);
           if (personList.length > 0) {
             resolve(personList[0]);
           }
         });
       }

       public queryPerson(predicates: relationalStore.RdbPredicates): Promise<Array<Person>> {
         console.info(TAG, 'queryPerson');
         return new Promise<Array<Person>>(async (resolve) => {
           let personList: Array<Person> = [];
           let resultSet = await rdbUtils.query(predicates);
           while (resultSet.goToNextRow()) {
             let person: Person = new Person();
             person.pId = resultSet.getString(resultSet.getColumnIndex('pId'));
             person.pName = resultSet.getString(resultSet.getColumnIndex('pName'));
             person.pAge = resultSet.getLong(resultSet.getColumnIndex('pAge'));
             personList.push(person);
           }
           resultSet.close();
           console.info(TAG, `queryPerson personList: ${JSON.stringify(personList)}`);
           resolve(personList);
         });
       }

       private generateBucket(person: Person): relationalStore.ValuesBucket {
         let valueBucket: relationalStore.ValuesBucket = {
           pId: person.pId,
           pName: person.pName,
           pAge: person.pAge
         };
         return valueBucket;
       }
     }
     ```
  3. 在应用的主页面中，创建刷新和保存按钮，从数据库获取并同步刷新最新数据。

     ```ts
     import { PersonRdbHelper } from '../utils/FormRdbHelper';
     import { Person } from '../viewmodel/Person';
     import { promptAction } from '@kit.ArkUI';

     @Entry
     @Component
     struct Index {
       @State num: number = 0;
       @State pId: string = '';
       @State pName: string = '';
       @State pAge: number = 0;
       context: Context = this.getUIContext().getHostContext()!.getApplicationContext();

       onPageShow(): void {
         this.calCount();
       }

       // 计算数据库总人数
       calCount() {
         let personRdbHelper = PersonRdbHelper.getInstance(this.context);
         //
         personRdbHelper.queryAllPerson().then((persons) => {
           this.num = persons.length;
         });
       }

       build() {
         Column({ space: 15 }) {
           Row({ space: 10 }) {
             Text(`当前班级总人数为${this.num}`)
               .fontSize(20);
             Button('刷新')
               .onClick(() => {
                 this.calCount();
               });
           }.width(250);

           Column({ space: 15 }) {
             Row() {
               Text('学号')
                 .fontSize(20);
               TextInput()
                 .width(200).fontSize(20).onChange((value) => {
                 this.pId = value;
               });
             }.width('100%');

             Row() {
               Text('姓名')
                 .fontSize(20);
               TextInput().width(200).fontSize(20).onChange((value) => {
                 this.pName = value;
               });
             }.width('100%');

             Row() {
               Text('年龄')
                 .fontSize(20);
               TextInput().width(200).type(InputType.Number).fontSize(20).onChange((value) => {
                 this.pAge = Number(value);
               });
             }.width('100%');

             Button('保存至数据库').onClick(async () => {
               let personRdbHelper = PersonRdbHelper.getInstance(this.context);
               let res = await personRdbHelper.insertPerson({
                 pId: this.pId,
                 pName: this.pName,
                 pAge: this.pAge
               } as Person);
               if (res > 0) {
                 promptAction.openToast({ message: '添加成功' });
               } else {
                 promptAction.openToast({ message: '添加失败' });
               }
               // 重新计算总数
               this.calCount();
             }).width('100%');
           }.width(250);
         }
         .height('100%')
         .width('100%');
       }
     }
     ```
  4. 编写卡片EntryFormAbility生命周期文件。定义calCount函数计算数据库总人数并查询最后一个人信息，刷新卡片。

     ```ts
     import { formBindingData, FormExtensionAbility, formInfo, formProvider } from '@kit.FormKit';
     import { Want } from '@kit.AbilityKit';
     import { PersonRdbHelper } from '../utils/FormRdbHelper';

     export default class EntryFormAbility extends FormExtensionAbility {
       // 计算数据库总人数
       async calCount(formId: string) {
         let personRdbHelper = PersonRdbHelper.getInstance(this.context.getApplicationContext());
         personRdbHelper.queryAllPerson().then(persons => {
           let num = persons.length;
           // 封装数据
           if (num > 0) {
             let formInfo = formBindingData.createFormBindingData({
               num: num,
               pId: persons[num - 1].pId,
               pName: persons[num - 1].pName,
               pAge: persons[num - 1].pAge
             });
             // 调用updateForm更新form
             formProvider.updateForm(formId, formInfo);
           }
         });
       }

       onAddForm(want: Want) {
         if (want.parameters) {
           let formId = want.parameters['ohos.extra.param.key.form_identity'] as string;
           this.calCount(formId);
         }
         return formBindingData.createFormBindingData({});
       }

       onUpdateForm(formId: string) {
         this.calCount(formId);
       }

       onFormEvent(formId: string) {
         this.calCount(formId);
       }

       onAcquireFormState() {
         return formInfo.FormState.READY;
       }
     };
     ```
  5. 在卡片页面中，渲染查询数据库的信息。创建刷新按钮，通过postCardAction完成刷新。

     ```ts
     @Entry
     @Component
     struct WidgetCard {
       @LocalStorageProp('num') num: number = 0;
       @LocalStorageProp('pId') pId: string = '还没数据';
       @LocalStorageProp('pName') pName: string = '还没数据';
       @LocalStorageProp('pAge') pAge: number = 0;

       build() {
         Column({ space: 15 }) {
           Row({ space: 10 }) {
             Text(`当前班级总人数为${this.num}`)
               .fontSize(20);
           }.width(250);

           Column({ space: 15 }) {
             Row() {
               Text(`最后一位同学学号：${this.pId}`)
                 .fontSize(20);
             }.width('100%');

             Row() {
               Text(`最后一位同学姓名：${this.pName}`)
                 .fontSize(20);
             }.width('100%');

             Row() {
               Text(`最后一位同学年龄：${this.pAge}`)
                 .fontSize(20);
             }.width('100%');

             Button('刷新').onClick(() => {
               postCardAction(this, {
                 action: 'message',
               });
             }).width('100%');
           }.width(250);
         }
         .justifyContent(FlexAlign.Center)
         .padding(16)
         .height('100%')
         .width('100%');
       }
     }
     ```

## 常见FAQ

Q：是否可以使用PersistentStorage和AppStorage在应用和卡片之间进行共享持久化数据？

A：卡片和应用的主进程不是一个进程，而AppStorage是和进程绑定的，仅支持应用的主线程内多个UIAbility实例间的UI状态数据共享，所以卡片和应用主进程之间无法使用PersistentStorage和AppStorage进行状态数据共享。

Q：使用用户首选项(Preferences)共享持久化数据时，查询/更新数据时为什么每次都需要执行removePreferencesFromCache操作？

A：不同进程的内存不共享，同一进程中getPreferences只有首次会从持久化中取，所以要跨进程读取最新的持久化数据时，需先通过removePreferencesFromCache接口将Preferences实例移出缓存中的实例之后，再次getPreferences将会重新读取持久化文件，生成新的Preferences实例。

Q：为什么调用getPreferencesSync获取首选项实例时，传入的context对象为应用级的？

A：主应用和卡片属于不同的进程，不同进程的context不同。为了保证主应用和卡片获取同一个首选项实例，传入的参数应该为应用级context。

## 总结

| 方案 | 说明 |
| --- | --- |
| 使用用户首选项共享持久化数据 | 用于Key-Value键值型的数据处理。 |
| 使用关系型数据库共享持久化数据 | 用于复杂关系数据的场景。 |
