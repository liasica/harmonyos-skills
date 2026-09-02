---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-local-database-management-59
title: 关系型数据库如何存取bigint型数据
breadcrumb: FAQ > 应用框架开发 > 本地数据和文件 > 本地数据库管理 > 关系型数据库如何存取bigint型数据
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:29+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:d04377a76b6f9f0b85a1dd1d3e30cc15959a03d850c107bb6f9bbdbeeb771851
---

## 问题现象

关系型数据库如何正确存取BigInt型数据，保证其精度不丢失？

## 背景知识

[ValueType](../harmonyos-references/arkts-apis-data-relationalstore-t.md#valuetype)：用于表示允许的数据字段类型，接口参数具体类型根据其功能而定。其类型支持bigint（值类型为任意长度的整数），使用bigint时需注意以下几点：

* 当字段类型是bigint时，在创建表的sql语句中，类型应当为：UNLIMITED INT。
* bigint类型当前不支持比较大小，不支持如下谓词：between、notBetween、greaterThanlessThan、greaterThanOrEqualTo、lessThanOrEqualTo、orderByAsc、orderByDesc。
* bigint类型字段的数据写入时，需通过BigInt()方法或在数据尾部添加'n'的方式明确为BigInt类型，如'let data = BigInt(1234)'或'let data = 1234n'。
* bigint字段如果写入number类型的数据，则查询该数据的返回类型为number，而非bigint。

## 解决方案

1. 数据库建表时声明BigInt数据类型为：UNLIMITED INT。
2. 构造数据插入表中，使用BigInt()生成BigInt型数据。
3. 查询数据库，使用[resultSet.getValue()](../harmonyos-references/arkts-apis-data-relationalstore-resultset.md#getvalue12)获取BigInt型数据。

完整示例参考如下：

```screen
import { relationalStore } from "@kit.ArkData";
import { common } from "@kit.AbilityKit";
import { BusinessError, systemDateTime } from "@kit.BasicServicesKit";

@Entry
@Component
struct BigintRdbDemo {
  @State message: string | undefined = undefined;
  private context = this.getUIContext().getHostContext() as common.UIAbilityContext;
  private promptAction = this.getUIContext().getPromptAction();
  private storeConfig: relationalStore.StoreConfig = {
    name: "BigintRdbDemo.db",
    securityLevel: relationalStore.SecurityLevel.S1,
  };
  store: relationalStore.RdbStore | undefined = undefined;

  build() {
    Column({ space: 20 }) {

      Text(this.message || 'Hello World!');

      Button('初始化数据库表')
        .width(150)
        .type(ButtonType.ROUNDED_RECTANGLE)
        .backgroundColor('#0a59f7')
        .onClick(() => {
          relationalStore.getRdbStore(this.context, this.storeConfig, (err, store) => {
            if (err) {
              console.error(`Failed to get RdbStore. Code:${err.code}, message:${err.message}`);
              this.promptAction.showToast({ message: '初始化数据库失败' });
              return;
            }
            console.info('Succeeded in getting RdbStore.');
            this.store = store;

            // step1：建表时声明BigInt数据类型为：UNLIMITED INT
            const sqlCreateTable =
              'CREATE TABLE IF NOT EXISTS EMPLOYEE (ID INTEGER PRIMARY KEY AUTOINCREMENT, IDENTITY UNLIMITED INT)';
            store.executeSql(sqlCreateTable) // 创建数据表，以便后续调用insert接口插入数据
              .then(() => {
                this.promptAction.showToast({ message: '初始化数据库表成功' });
              })
              .catch((err: BusinessError) => {
                this.promptAction.showToast({ message: '初始化数据库表失败' });
                console.error(`Failed to executeSql. Code:${err.code}, message:${err.message}`);
              });
          });
        });

      Button('插入bigInt类型数据')
        .width(150)
        .type(ButtonType.ROUNDED_RECTANGLE)
        .backgroundColor('#0a59f7')
        .onClick(() => {
          let time = systemDateTime.getTime(true);
          let dataList = new Array<relationalStore.ValuesBucket>();
          for (let index = 0; index < 10; index++) {
            let data: relationalStore.ValuesBucket = {
              // step2：构造数据插入表中，使用BigInt()生成bigInt类型数据
              "IDENTITY": BigInt(time * 10000 + index)
            };
            dataList.push(data);
          }
          this.store?.batchInsert("EMPLOYEE", dataList, (err, ret) => {
            if (err) {
              this.promptAction.showToast({ message: '数据插入失败' });
              console.error(`insertData() failed, err.message: ${err.message}, err.code: ${err.code}`);
              return;
            }
            this.promptAction.showToast({ message: '数据插入成功' });
            console.info(`insertData() finished: ${ret}`);
          });
        });

      Button('查询bigInt类型数据')
        .width(150)
        .type(ButtonType.ROUNDED_RECTANGLE)
        .backgroundColor('#0a59f7')
        .onClick(() => {
          this.store?.querySql("select * from EMPLOYEE limit 1", (err, resultSet) => {
            if (err) {
              this.promptAction.showToast({ message: '数据查询失败' });
              console.error(`Query failed, code is ${err.code},message is ${err.message}`);
              return;
            }
            // resultSet是一个数据集合的游标，默认指向第-1个记录，有效的数据从0开始。
            while (resultSet.goToNextRow()) {
              const id = resultSet.getLong(resultSet.getColumnIndex("ID"));
              // step3：查询数据库，使用resultSet.getValue()获取BigInt型数据。
              const identity = resultSet.getValue(resultSet.getColumnIndex("IDENTITY"));
              this.message = identity?.toString();
              console.info(`id=${id}, identity=${identity}`);
            }
            this.promptAction.showToast({ message: '数据查询成功' });
            // 释放数据集的内存
            resultSet.close();
          });
        });
    }
    .justifyContent(FlexAlign.Center)
    .height('100%')
    .width('100%');
  }
}
```
