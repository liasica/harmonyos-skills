---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-local-database-management-17
title: 如何通过谓词查询方式获取数据
breadcrumb: FAQ > 应用框架开发 > 本地数据和文件 > 本地数据库管理 > 如何通过谓词查询方式获取数据
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:29+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:9b68df4bd3a468f10baaa71ff806c5ddc6efa2a5ca3d4b98ec7da7e392c7a2df
---

[getEntries()](../harmonyos-references/js-apis-distributedkvstore.md#getentries-3)可以使用谓词查询，根据谓词查询的方式批量获取value，如使用like，unlike，isnull等方法。

参考代码如下：

```ts
import { BusinessError } from '@kit.BasicServicesKit';
import { distributedKVStore } from '@kit.ArkData';

let kvStore: undefined | distributedKVStore.SingleKVStore = undefined;

@Entry
@Component
export struct ReadingTheLocalDatabase {
  build() {
    Row() {
      Column({ space: 20 }) {
        Button('Create database')
          .fontSize(20)
          .fontWeight(FontWeight.Bold)
          .onClick(async () => {
            try {
              let name = new distributedKVStore.FieldNode('name'); // Create FieldNode
              name.type = distributedKVStore.ValueType.STRING; // Set NodeType string
              name.nullable = false; // NodeData is not null
              name.default = 'cake'; // Default

              let schema1 = new distributedKVStore.Schema(); // Create Schema
              schema1.root.appendChild(name); // add Child name
              schema1.indexes = ['$.name'];
              // Create KVManager
              let kvManager = distributedKVStore.createKVManager({
                bundleName: 'TEST_CRASH_APP',
                context: this.getUIContext().getHostContext()
              });
              // Create database 
              await kvManager.getKVStore('storeIds', {
                createIfMissing: true,
                backup: false,
                encrypt: false,
                autoSync: false,
                schema: schema1,
                kvStoreType: distributedKVStore.KVStoreType.SINGLE_VERSION,
                securityLevel: distributedKVStore.SecurityLevel.S2
              }).then((store: distributedKVStore.SingleKVStore) => {
                kvStore = store;
              }).catch((err: BusinessError) => {
                console.info(`getKVStore error is: ${err.code}, msg is: ${err.message}`);
              })
              if (kvStore === undefined) {
                return;
              }
              let entries: distributedKVStore.Entry[] = [];
              for (let i = 0; i < 10; i++) {
                let ent: distributedKVStore.Entry = {
                  key: 'test' + i,
                  value: {
                    type: distributedKVStore.ValueType.STRING,
                    value: '{"name":"cake"}'
                  }
                }
                entries.push(ent);
              }
              // insert data 
              kvStore.putBatch(entries)
                .then((data) => {
                  console.info('Succeeded in putting Batch');
                })
                .catch((err: BusinessError) => {
                  console.info(`putBatch error is: ${err.code}, msg is: ${err.message}`);
                })
            } catch (e) {
              console.info(`putBatch e is: ${e.code}, msg is: ${e.message}`);
            }
          })

        Button('like select')
          .fontSize(20)
          .onClick(() => {
            try {
              if (kvStore === undefined) {
                return;
              }
              // Use predicates to query a specified field that has a value similar to the specified string, and obtain a list of key value pairs that match the specified Query object
              kvStore.getEntries(new distributedKVStore.Query().like('$.name', 'c%'))
                .then((value) => {
                  for (let i = 0; i < value.length; i++) {
                    console.info('key:' + value[i].key + 'value : ' + JSON.stringify(value[i].value))
                  }
                })
                .catch((err: BusinessError) => {
                  console.info(`getEntries error is: ${err.code}, msg is: ${err.message}`);
                })
            } catch (e) {
              console.info(`getEntries e is: ${e.code}, msg is: ${e.message}`);
            }
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}
```
