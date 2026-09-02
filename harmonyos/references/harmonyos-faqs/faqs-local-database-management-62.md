---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-local-database-management-62
title: 如何将数据库的中number类型升级为BigInt
breadcrumb: FAQ > 应用框架开发 > 本地数据和文件 > 本地数据库管理 > 如何将数据库的中number类型升级为BigInt
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:29+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:2a4c7ed5f5956b1d83086e518668bde898af377428f2c9ed04627a83ebf67619
---

## 问题现象

在关系型数据库中，如何将数据库中原有number类型的数据升级为BigInt类型？

## 背景知识

* [关系型数据库](../harmonyos-guides/data-persistence-by-rdb-store.md)：ArkTS关系型数据库基于SQLite实现，为应用提供数据持久化能力。
* [ValueType](../harmonyos-references/arkts-apis-data-relationalstore-t.md#valuetype)：用于表示允许的数据字段类型，接口参数具体类型根据其功能而定。
* BigInt表示值类型为任意长度的整数。当字段类型是BigInt时，在创建表的sql语句中，类型应当为：UNLIMITED INT。
  + BigInt类型当前不支持比较大小，不支持如下谓词：between、notBetween、greaterThanlessThan、greaterThanOrEqualTo、lessThanOrEqualTo、orderByAsc、orderByDesc。
  + BigInt类型字段的数据写入时，需通过BigInt()方法或在数据尾部添加'n'的方式明确为BigInt类型，如'let data = BigInt(1234)'或'let data = 1234n'。
  + BigInt字段如果写入number类型的数据，则查询该数据的返回类型为number，而非BigInt。

## 解决方案

在数据库中将原有的数据类型转换为其他类型，需要用sql语句实现，具体步骤如下：

1. 将旧表重命名。
2. 创建新表结构，使用UNLIMITED INT类型替换需要转换的字段。
3. 将旧表数据迁移到新表，使用CAST(原列AS UNLIMITED INT)确保数据无损转换。
4. 删除旧表。

代码示例如下：

```ts
async changeDbDataType() {
  // 注意：SQLite不支持简单的ALTER COLUMN来改变类型，以下是一个常见的替代方案
  if (this.rdbStore) {
    try {
      // 1.将旧表重命名
      await this.rdbStore.executeSql('ALTER TABLE Student RENAME TO old_Student;');
      // 2.创建新表结构，使用UNLIMITED INT类型
      const CREATE_TABLE_SQL = 'CREATE TABLE IF NOT EXISTS Student (' +
        'id INTEGER PRIMARY KEY AUTOINCREMENT, ' +
        'name TEXT NOT NULL, ' +
        'age INTEGER, ' +
        'identity UNLIMITED INT DEFAULT 1234567898888888, ' +
        'carId  UNLIMITED INT DEFAULT 123456789, ' +
        'salary REAL)';
      await this.rdbStore.executeSql(CREATE_TABLE_SQL);
      // 3.将旧表数据迁移到新表，使用CAST(原列AS UNLIMITED INT)确保数据无损转换
      const INSERT_SQL = 'INSERT INTO Student (id, name, age, identity, carId, salary) ' +
        'SELECT id, name, age, identity, CAST(carId AS UNLIMITED INT), ' +
        'salary FROM old_Student;';
      await this.rdbStore.executeSql(INSERT_SQL);
      // 4.删除旧表
      await this.rdbStore.executeSql('DROP TABLE old_Student');
      console.info('数据库表结构升级完成，字段类型已改为BigInt');
    } catch (err) {
      console.error(`changeDbDataType failed, code is ${err.code},message is ${err.message}`);
    }
  }
}
```

完整代码示例如下：

```ts
import { relationalStore } from '@kit.ArkData';
import { common } from '@kit.AbilityKit';
import { BusinessError } from '@ohos.base';

@Entry
@Component
struct Index {
  rdbStore: relationalStore.RdbStore | undefined = undefined;
  context: Context = this.getUIContext().getHostContext() as common.UIAbilityContext;

  async create(context: Context) {
    const CONFIG: relationalStore.StoreConfig = {
      name: 'Student.db',
      securityLevel: relationalStore.SecurityLevel.S1,
    };
    relationalStore.getRdbStore(context, CONFIG, async (err: BusinessError, rdbStore: relationalStore.RdbStore) => {
      this.rdbStore = rdbStore;
      if (err) {
        console.error(`Get RdbStore failed, code is ${err.code},message is ${err.message}`);
        return;
      }
      console.info(`Create Student.db successfully!`);
      // 创建表，在创建表时，通过DEFAULT关键字为bigint列设置默认值
      const CREATE_TABLE_SQL = 'CREATE TABLE IF NOT EXISTS Student (' +
        'id INTEGER PRIMARY KEY AUTOINCREMENT, ' +
        'name TEXT NOT NULL, ' +
        'age INTEGER, ' +
        'identity UNLIMITED INT DEFAULT 1234567898888888, ' +
        'carId INTEGER, ' +
        'salary REAL)';
      await this.rdbStore.executeSql(CREATE_TABLE_SQL);
      console.info(`Create table test successfully!`);
    });
  }

  async insert(valueBucketArray: Array<relationalStore.ValuesBucket>) {
    // 数据插入
    if (this.rdbStore) {
      await this.rdbStore.batchInsert('Student', valueBucketArray);
      console.info(`insert data successfully!`);
    }
  }

  async query() {
    // 获取结果集
    if (this.rdbStore) {
      let predicates: relationalStore.RdbPredicates = new relationalStore.RdbPredicates('Student');
      let resultSet = await this.rdbStore.query(predicates); // 查询所有数据
      console.info(`Query data successfully! row count:${resultSet.rowCount}`);
      while (resultSet.goToNextRow()) {
        const id = resultSet.getLong(resultSet.getColumnIndex('id'));
        const name = resultSet.getString(resultSet.getColumnIndex('name'));
        const age = resultSet.getLong(resultSet.getColumnIndex('age'));
        const carId = resultSet.getValue(resultSet.getColumnIndex('carId'));
        const identity = resultSet.getValue(resultSet.getColumnIndex('identity')) as bigint;
        const salary = resultSet.getDouble(resultSet.getColumnIndex('SALARY'));
        console.info(`id=${id}, name=${name}, age=${age},carId=${carId}, identity=${identity}, salary=${salary}`);
      }
      // 释放数据集的内存
      resultSet.close();
    }
  }

  async changeDbDataType() {
    // 注意：SQLite不支持简单的ALTER COLUMN来改变类型，以下是一个常见的替代方案
    if (this.rdbStore) {
      try {
        // 1.将旧表重命名
        await this.rdbStore.executeSql('ALTER TABLE Student RENAME TO old_Student;');
        // 2.创建新表结构，使用UNLIMITED INT类型
        const CREATE_TABLE_SQL = 'CREATE TABLE IF NOT EXISTS Student (' +
          'id INTEGER PRIMARY KEY AUTOINCREMENT, ' +
          'name TEXT NOT NULL, ' +
          'age INTEGER, ' +
          'identity UNLIMITED INT DEFAULT 1234567898888888, ' +
          'carId  UNLIMITED INT DEFAULT 123456789, ' +
          'salary REAL)';
        await this.rdbStore.executeSql(CREATE_TABLE_SQL);
        // 3.将旧表数据迁移到新表，使用CAST(原列AS UNLIMITED INT)确保数据无损转换
        const INSERT_SQL = 'INSERT INTO Student (id, name, age, identity, carId, salary) ' +
          'SELECT id, name, age, identity, CAST(carId AS UNLIMITED INT), ' +
          'salary FROM old_Student;';
        await this.rdbStore.executeSql(INSERT_SQL);
        // 4.删除旧表
        await this.rdbStore.executeSql('DROP TABLE old_Student');
        console.info('数据库表结构升级完成，字段类型已改为BigInt');
      } catch (err) {
        console.error(`changeDbDataType failed, code is ${err.code},message is ${err.message}`);
      }
    }
  }

  aboutToAppear(): void {
    this.create(this.context);
  }

  build() {
    Row() {
      Column() {
        Button('插入数据')
          .margin({ top: 10 })
          .onClick(() => {
            // 模拟数据
            const count = 2;
            const timeCount = new Date().getTime();
            let valueBucketArray = new Array<relationalStore.ValuesBucket>(count);
            for (let i = 0; i < count; i++) {
              // identity不做设置，数据库显示默认值
              let v: relationalStore.ValuesBucket = {
                id: timeCount + i,
                name: 'zhangsan' + i,
                age: 20 + i,
                carId: 3000 + 30 * i,
                salary: 5000 + 50 * i
              };
              valueBucketArray[i] = v;
            }
            this.insert(valueBucketArray);
          })
        Button('修改数据类型')
          .margin({ top: 10 })
          .onClick(() => {
            this.changeDbDataType();
          })
        Button('插入新类型数据')
          .margin({ top: 10 })
          .onClick(() => {
            let count = 3;
            const timeCount = new Date().getTime();
            let valueBucketArray = new Array<relationalStore.ValuesBucket>(count);
            for (let i = 0; i < count; i++) {
              let v: relationalStore.ValuesBucket = {
                id: timeCount + i,
                name: 'lisi' + i,
                age: 15 + i,
                carId: BigInt('666666666000000000' + i),
                identity: BigInt('123456789000000000' + i),
                salary: 5000 + 50 * i
              };
              valueBucketArray[i] = v;
            }
            this.insert(valueBucketArray);
          })
        Button('查询数据')
          .margin({ top: 10 })
          .onClick(() => {
            this.query();
          })
      }
      .width('100%')
      .margin({ top: 10 })
      .justifyContent(FlexAlign.SpaceAround)
    }
    .height('100%')
    .width('100%')
  }
}
```

## 常见FAQ

Q：在创建数据库时，如何指定BigInt默认值？

A：在创建表时，通过DEFAULT关键字为BigInt列设置默认值。代码示例如下：

```ts
const CREATE_TABLE_SQL = 'CREATE TABLE IF NOT EXISTS Student (' +
  'id INTEGER PRIMARY KEY AUTOINCREMENT, ' +
  'name TEXT NOT NULL, ' +
  'age INTEGER, ' +
  'identity UNLIMITED INT DEFAULT 1234567898888888, ' +
  'carId  UNLIMITED INT DEFAULT 123456789, ' +
  'salary REAL)';
```

Q：如何读取数据库的BigInt数据？

A：可以使用getValue接口来获取。代码示例如下：

```ts
const carId = resultSet.getValue(resultSet.getColumnIndex('carId'));
const identity = resultSet.getValue(resultSet.getColumnIndex('identity')) as bigint;
```
