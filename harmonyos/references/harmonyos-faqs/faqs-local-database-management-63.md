---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-local-database-management-63
title: 如何使用公共目录下的数据库文件
breadcrumb: FAQ > 应用框架开发 > 本地数据和文件 > 本地数据库管理 > 如何使用公共目录下的数据库文件
category: harmonyos-faqs
scraped_at: 2026-09-02T15:04:06+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:3e638f50a4cd750a6aae41090067ec9da56651704922c068a55691864cf75a14
---

## 问题现象

用户在公共目录下载保存了一个数据库文件，在应用内应该如何使用该数据库文件？

## 背景知识

* [关系型数据库](../harmonyos-references/js-apis-data-relationalstore.md)（Relational Database，RDB）是一种基于关系模型来管理数据的数据库。关系型数据库基于SQLite组件提供了一套完整的对本地数据库进行管理的机制，对外提供了一系列的增、删、改、查等接口，也可以直接运行用户输入的SQL语句来满足复杂的场景需要。
* [StoreConfig](../harmonyos-references/arkts-apis-data-relationalstore-i.md#storeconfig)中的属性rootDir可以指定数据库根路径。从API18开始，支持此可选参数。将从如下目录打开或删除数据库：${rootDir}/${customDir}。通过设置此参数打开的数据库为只读模式，不允许对数据库进行写操作，否则返回错误码801。配置此参数打开或删除数据库时，应确保对应路径下数据库文件存在，并且有读取权限，否则返回错误码14800010。
* 开发者可以通过系统预置的[文件选择器（FilePicker）](../harmonyos-references/js-apis-file-picker.md)，实现公共目录文件的选择和保存。通过Picker访问相关文件，将拉起对应的应用，引导用户完成界面操作，接口本身无需申请权限。Picker获取的URI只具有临时权限，获取持久化权限需要通过[FilePicker设置永久授权](../harmonyos-guides/file-persistpermission.md#通过picker获取临时授权并进行授权持久化)方式获取。
* 文件选择器[documentViewPicker](../harmonyos-references/js-apis-file-picker.md#documentviewpicker)适用于文件类型文件的选择与保存。

## 解决方案

需要使用公共目录下的数据库文件，主要有以下两种解决方案：

* 转存到应用沙箱内，完整使用该数据库文件：使用[documentViewPicker.select()](../harmonyos-references/js-apis-file-picker.md#select)获取公共目录数据库文件，使用[@ohos.file.fs (文件管理)](../harmonyos-references/js-apis-file-fs.md)的能力拷贝到沙箱目录后，即可使用[@ohos.data.relationalStore (关系型数据库)](../harmonyos-references/js-apis-data-relationalstore.md)对转存到沙箱目录的数据库文件进行完整操作。
* 使用@ohos.data.relationalStore (关系型数据库)的能力，配置rootDir、customDir使用**只读模式**打开该数据库文件：具体方案参照下文详细步骤。

本文主要介绍如何直接使用公共目录下的数据库文件。

1. 使用documentViewPicker.select()选择公共目录下的数据库文件。

   **说明** 

   * 关系型数据库至少需要.db、.db-shm、.db-wal三个文件，因此此处需要引导用户选择对应的这三个文件。
   * 该接口获取的URI权限是临时只读权限，待退出应用后台后，获取的临时权限就会失效。

   ```ts
   selectFile() {
     try {
       let documentSelectOptions = new picker.DocumentSelectOptions();
       documentSelectOptions.maxSelectNumber = 3;
       documentSelectOptions.fileSuffixFilters = ['.db', '.db-shm', '.db-wal'];
       documentSelectOptions.selectMode = picker.DocumentSelectMode.MIXED;
       let documentPicker = new picker.DocumentViewPicker(this.context);
       documentPicker.select(documentSelectOptions).then((result: Array<string>) => {
         console.info(`DocumentViewPicker.select successfully, result uri: ${JSON.stringify(result)}`);
         if (!result || result.length < 1) {
           console.warn(`未选择文件`);
           this.promptAction.showToast({ message: '请选择对应db、db-shm、db-wal文件' });
           return;
         }
         if (result.length < 3) {
           console.warn(`请选择必须的db、db-shm、db-wal文件`);
           this.promptAction.showToast({ message: '请选择对应db、db-shm、db-wal文件' });
           return;
         }
         // 持久化授权：如果是 /storage/Users/currentUser/Download/应用包名 目录下的文件无需持久化授权即可使用
         this.persistPermission(result);
         // 获取其中的db文件名、rootDir、customDir
         this.resolveDbMessage(result);
         this.promptAction.showToast({ message: `选择成功！` });
       }).catch((err: BusinessError) => {
         console.error(`documentPicker select failed, code is ${err.code},message is ${err.message}`);
       });
     } catch (e) {
       let err = e as BusinessError;
       console.error(`selectFile failed, code is ${err.code},message is ${err.message}`);
     }
   }
   ```
2. 使用[fileShare.persistPermission()](../harmonyos-references/js-apis-fileshare.md#filesharepersistpermission11)对上述选择的文件URI进行持久化授权，需在module.json5文件中配置ohos.permission.FILE\_ACCESS\_PERSIST权限。数据库只读场景至少需要有.db、.db-shm、.db-wal这三个文件的可读权限。

   **说明** 

   * 持久化授权需要ohos.permission.FILE\_ACCESS\_PERSIST权限，该权限属于ACL受限权限，需要参考[申请受限权限](../harmonyos-guides/declare-permissions-in-acl.md)进行申请。
   * 持久化授权的数据存储在系统的数据库中，应用或者设备重启后需要使用[fileShare.activatePermission()](../harmonyos-references/js-apis-fileshare.md#fileshareactivatepermission11)激活已持久化的授权才可以正常使用激活持久化授权。
   * 对于DOWNLOAD/应用包名对应的公共目录路径，应用无需使用持久化授权即可获得读取权限。

   ```json
   {
     "name": "ohos.permission.FILE_ACCESS_PERSIST"
   },
   ```

   ```ts
   persistPermission(uris: Array<string>) {
     try {
       // 获取已授权uri，对未授权uri重新授权
       let policyUris = this.dataPreferences.getSync('policyUris', []) as Array<string>;
       if (policyUris && policyUris.length > 0) {
         uris.filter((uri) => {
           // 过滤已授权uri
           return !policyUris.includes(uri);
         });
       }
       let policies: Array<fileShare.PolicyInfo> = [];
       uris.forEach((uri: string) => {
         let policyInfo: fileShare.PolicyInfo = {
           uri: uri,
           operationMode: fileShare.OperationMode.READ_MODE,
         };
         policies.push(policyInfo);
       });
       // 持久化授权：需在module.json5文件中配置ohos.permission.FILE_ACCESS_PERSIST权限
       fileShare.persistPermission(policies).then(() => {
         console.info(`persistPermission successfully. policies: ${JSON.stringify(policies)}`);
         // 授权成功，保存已授权uri
         let policyUris = this.dataPreferences.getSync('policyUris', []) as Array<string>;
         if (policyUris) {
           policyUris.push(...uris);
         }
         this.dataPreferences.putSync('policyUris', policyUris);
         this.dataPreferences.flushSync();
       }).catch((err: BusinessError<Array<fileShare.PolicyErrorResult>>) => {
         console.error(`persistPermission failed with error message: ${err.message}, error code: ${err.code}`);
         if (err.code == 13900001 && err.data) {
           for (let i = 0; i < err.data.length; i++) {
             console.error(`error code : ${JSON.stringify(err.data[i].code)}`);
             console.error(`error uri : ${JSON.stringify(err.data[i].uri)}`);
             console.error(`error reason : ${JSON.stringify(err.data[i].message)}`);
           }
         }
       });
     } catch (error) {
       let err: BusinessError = error as BusinessError;
       console.error(`persistPermission failed with err, Error code: ${err.code}, message: ${err.message}`);
     }
   }
   ```
3. 提取公共目录下对应的db文件名、rootDir、customDir，使用[relationalStore.getRdbStore()](../harmonyos-references/arkts-apis-data-relationalstore-f.md#relationalstoregetrdbstore)以只读模式打开对应数据库，即可读取公共目录的数据库文件内容。

   ```ts
   initRdb() {
     try {
       /**
        * 直接使用公共目录下数据库文件至少需要.db、.db-shm、.db-wal，所以在实际开库使用前需要提前校验是否有这对应三个文件的可读权限
        */
       if (!this.checkUirPermission()) {
         console.warn(`校验未通过，请重新选择必要的db、db-shm、db-wal文件.`);
         return;
       }
       let dbConfig: relationalStore.StoreConfig = {
         name: this.dbName,
         securityLevel: relationalStore.SecurityLevel.S3,
         rootDir: this.rootDir,
         customDir: this.customDir
       };
       console.info(`dbName: ${this.dbName}, rootDir: ${this.rootDir}, customDir: ${this.customDir}`);
       // 1.获取公共目录下的数据库文件，使用只读模式打开
       relationalStore.getRdbStore(this.context, dbConfig).then((rdbStore: relationalStore.RdbStore) => {
         this.store = rdbStore;
         try {
           if (rdbStore != undefined) {
             // 监听sql错误信息
             rdbStore.on('sqliteErrorOccurred', exceptionMessage => {
               let sqliteCode = exceptionMessage.code;
               let sqliteMessage = exceptionMessage.message;
               let errSQL = exceptionMessage.sql;
               console.error(`error log is ${sqliteCode}, errMessage is ${sqliteMessage}, errSQL is ${errSQL}`);
             });
           }
         } catch (err) {
           let code = (err as BusinessError).code;
           let message = (err as BusinessError).message;
           console.error(`Register observer failed, code is ${code},message is ${message}`);
         }
         this.promptAction.showToast({ message: `数据库初始化成功.` });
         console.info('initRdb successfully.');
       }).catch((err: BusinessError) => {
         console.error(`initRdb failed, code is ${err.code},message is ${err.message}`);
       });
     } catch (err) {
       console.error(`initRdb failed, code is ${err.code},message is ${err.message}`);
     }
   }
   ```

完整示例参考如下，需在module.json5文件中配置ohos.permission.FILE\_ACCESS\_PERSIST权限（实际运行需提前将数据库对应的db文件、db-shm文件、db-wal文件预置在设备的公共目录下）：

```ts
import { common } from '@kit.AbilityKit';
import { fileIo, fileShare, picker } from '@kit.CoreFileKit';
import { preferences, relationalStore } from '@kit.ArkData';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  private rootDir: string = '';
  private customDir: string = '';
  private dbName: string = '';
  private tableName: string = 'testTable'; // 表名，根据实际修改
  private context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
  private promptAction = this.getUIContext().getPromptAction();
  private store: relationalStore.RdbStore | undefined = undefined;
  private dataPreferences = preferences.getPreferencesSync(this.context, { name: 'test' });

  aboutToAppear(): void {
    try {
      // 重新激活持久化授权
      this.activatePermission();

      // 获取上次打开的公共目录
      this.rootDir = this.dataPreferences.getSync('rootDir', '') as string;
      this.customDir = this.dataPreferences.getSync('customDir', '') as string;
      this.dbName = this.dataPreferences.getSync('dbName', '') as string;
    } catch (error) {
      let err: BusinessError = error as BusinessError;
      console.error(`activatePermission failed with error message: ${err.message}, error code: ${err.code}`);
    }
  }

  activatePermission() {
    try {
      // 获取已授权uri，重新激活授权
      let policyUris = this.dataPreferences.getSync('policyUris', []) as Array<string>;
      if (policyUris && policyUris.length > 0) {
        let policies: Array<fileShare.PolicyInfo> = [];
        policyUris.forEach((uri: string) => {
          let policyInfo: fileShare.PolicyInfo = {
            uri: uri,
            operationMode: fileShare.OperationMode.READ_MODE,
          };
          policies.push(policyInfo);
        });
        // 重新激活持久化授权：需在module.json5文件中配置ohos.permission.FILE_ACCESS_PERSIST权限
        fileShare.activatePermission(policies).then(() => {
          console.info(`activatePermission successfully, policies: ${JSON.stringify(policies)}`);
        }).catch(async (err: BusinessError<Array<fileShare.PolicyErrorResult>>) => {
          console.error(`activatePermission failed with error message: ${err.message}, error code: ${err.code}`);
          if (err.code == 13900001 && err.data) {
            for (let i = 0; i < err.data.length; i++) {
              console.error(`error code : ${JSON.stringify(err.data[i].code)}`);
              console.error(`error uri : ${JSON.stringify(err.data[i].uri)}`);
              console.error(`error reason : ${JSON.stringify(err.data[i].message)}`);
              if (err.data[i].code == fileShare.PolicyErrorCode.PERMISSION_NOT_PERSISTED) {
                await fileShare.persistPermission(policies);
              }
            }
          }
        });
      }
    } catch (error) {
      let err: BusinessError = error as BusinessError;
      console.error(`activatePermission failed with error message: ${err.message}, error code: ${err.code}`);
    }
  }

  build() {
    Column({ space: 20 }) {
      Button('选择公共目录下的数据库文件')
        .onClick(() => {
          this.selectFile();
        });

      Button('初始化数据库实例')
        .onClick(() => {
          this.initRdb();
        });

      Button('查询数据')
        .onClick(() => {
          this.queryData();
        });
    }
    .justifyContent(FlexAlign.Center)
    .height('100%')
    .width('100%');
  }

  selectFile() {
    try {
      let documentSelectOptions = new picker.DocumentSelectOptions();
      documentSelectOptions.maxSelectNumber = 3;
      documentSelectOptions.fileSuffixFilters = ['.db', '.db-shm', '.db-wal'];
      documentSelectOptions.selectMode = picker.DocumentSelectMode.MIXED;
      let documentPicker = new picker.DocumentViewPicker(this.context);
      documentPicker.select(documentSelectOptions).then((result: Array<string>) => {
        console.info(`DocumentViewPicker.select successfully, result uri: ${JSON.stringify(result)}`);
        if (!result || result.length < 1) {
          console.warn(`未选择文件`);
          this.promptAction.showToast({ message: '请选择对应db、db-shm、db-wal文件' });
          return;
        }
        if (result.length < 3) {
          console.warn(`请选择必须的db、db-shm、db-wal文件`);
          this.promptAction.showToast({ message: '请选择对应db、db-shm、db-wal文件' });
          return;
        }
        // 持久化授权：如果是 /storage/Users/currentUser/Download/应用包名 目录下的文件无需持久化授权即可使用
        this.persistPermission(result);
        // 获取其中的db文件名、rootDir、customDir
        this.resolveDbMessage(result);
        this.promptAction.showToast({ message: `选择成功！` });
      }).catch((err: BusinessError) => {
        console.error(`documentPicker select failed, code is ${err.code},message is ${err.message}`);
      });
    } catch (e) {
      let err = e as BusinessError;
      console.error(`selectFile failed, code is ${err.code},message is ${err.message}`);
    }
  }

  resolveDbMessage(result: string[]) {
    try {
      result.forEach((uri: string) => {
        if (uri.endsWith('.db')) {
          // 从公共目录文件路径获取数据库文件名及父目录路径等必要参数
          this.dbName = uri.split('/').pop() || '';
          let file = fileIo.openSync(uri, fileIo.OpenMode.READ_ONLY);
          let parent = file.getParent();
          console.info(`parent: ${parent}`);
          fileIo.closeSync(file);
          if (parent.includes('/')) {
            this.rootDir = parent.substring(0, parent.lastIndexOf('/'));
          }
          this.customDir = parent.split('/').pop() || '';

          // 存储公共目录数据库必要参数，以便下次直接使用
          this.dataPreferences.putSync('dbName', this.dbName);
          this.dataPreferences.putSync('rootDir', this.rootDir);
          this.dataPreferences.putSync('customDir', this.customDir);
          this.dataPreferences.flushSync();
          console.info(`dbName: ${this.dbName}, rootDir: ${this.rootDir}, customDir: ${this.customDir}`);
        }
      });
    } catch (e) {
      let err = e as BusinessError;
      console.error(`resolveDbMessage failed, code is ${err.code},message is ${err.message}`);
    }
  }

  persistPermission(uris: Array<string>) {
    try {
      // 获取已授权uri，对未授权uri重新授权
      let policyUris = this.dataPreferences.getSync('policyUris', []) as Array<string>;
      if (policyUris && policyUris.length > 0) {
        uris.filter((uri) => {
          // 过滤已授权uri
          return !policyUris.includes(uri);
        });
      }
      let policies: Array<fileShare.PolicyInfo> = [];
      uris.forEach((uri: string) => {
        let policyInfo: fileShare.PolicyInfo = {
          uri: uri,
          operationMode: fileShare.OperationMode.READ_MODE,
        };
        policies.push(policyInfo);
      });
      // 持久化授权：需在module.json5文件中配置ohos.permission.FILE_ACCESS_PERSIST权限
      fileShare.persistPermission(policies).then(() => {
        console.info(`persistPermission successfully. policies: ${JSON.stringify(policies)}`);
        // 授权成功，保存已授权uri
        let policyUris = this.dataPreferences.getSync('policyUris', []) as Array<string>;
        if (policyUris) {
          policyUris.push(...uris);
        }
        this.dataPreferences.putSync('policyUris', policyUris);
        this.dataPreferences.flushSync();
      }).catch((err: BusinessError<Array<fileShare.PolicyErrorResult>>) => {
        console.error(`persistPermission failed with error message: ${err.message}, error code: ${err.code}`);
        if (err.code == 13900001 && err.data) {
          for (let i = 0; i < err.data.length; i++) {
            console.error(`error code : ${JSON.stringify(err.data[i].code)}`);
            console.error(`error uri : ${JSON.stringify(err.data[i].uri)}`);
            console.error(`error reason : ${JSON.stringify(err.data[i].message)}`);
          }
        }
      });
    } catch (error) {
      let err: BusinessError = error as BusinessError;
      console.error(`persistPermission failed with err, Error code: ${err.code}, message: ${err.message}`);
    }
  }

  checkUirPermission() {
    try {
      if (!this.dbName) {
        this.promptAction.showToast({ message: '请选择必须的db、db-shm、db-wal文件' });
        console.warn(`请选择必须的db、db-shm、db-wal文件`);
        return false;
      }
      // 获取已授权uri，校验当前数据库必要文件是否已授权
      let policyUris = this.dataPreferences.getSync('policyUris', []) as Array<string>;
      if (!policyUris || policyUris.length < 3) {
        this.promptAction.showToast({ message: '请选择必须的db、db-shm、db-wal文件' });
        console.warn(`请选择必须的db、db-shm、db-wal文件`);
        return false;
      }
      let baseDir = `${this.rootDir}/${this.customDir}`;
      let dbPath = `${baseDir}/${this.dbName}`;
      let name = this.dbName.split('.')[0];
      if (!policyUris.some(uri => uri.endsWith(`${dbPath}`)) ||
        !policyUris.some(uri => uri.endsWith(`${baseDir}/${name}.db-shm`)) ||
        !policyUris.some(uri => uri.endsWith(`${baseDir}/${name}.db-wal`))) {
        this.promptAction.showToast({ message: '请选择必须的db、db-shm、db-wal文件' });
        console.warn(`请选择必须的db、db-shm、db-wal文件`);
        return false;
      }
      console.info(`checkUirPermission successful.`);
      return true;
    } catch (error) {
      let err: BusinessError = error as BusinessError;
      console.error(`checkUirPermission failed with err, Error code: ${err.code}, message: ${err.message}`);
      return false;
    }
  }

  initRdb() {
    try {
      /**
       * 直接使用公共目录下数据库文件至少需要.db、.db-shm、.db-wal，所以在实际开库使用前需要提前校验是否有这对应三个文件的可读权限
       */
      if (!this.checkUirPermission()) {
        console.warn(`校验未通过，请重新选择必要的db、db-shm、db-wal文件.`);
        return;
      }
      let dbConfig: relationalStore.StoreConfig = {
        name: this.dbName,
        securityLevel: relationalStore.SecurityLevel.S3,
        rootDir: this.rootDir,
        customDir: this.customDir
      };
      console.info(`dbName: ${this.dbName}, rootDir: ${this.rootDir}, customDir: ${this.customDir}`);
      // 1.获取公共目录下的数据库文件，使用只读模式打开
      relationalStore.getRdbStore(this.context, dbConfig).then((rdbStore: relationalStore.RdbStore) => {
        this.store = rdbStore;
        try {
          if (rdbStore != undefined) {
            // 监听sql错误信息
            rdbStore.on('sqliteErrorOccurred', exceptionMessage => {
              let sqliteCode = exceptionMessage.code;
              let sqliteMessage = exceptionMessage.message;
              let errSQL = exceptionMessage.sql;
              console.error(`error log is ${sqliteCode}, errMessage is ${sqliteMessage}, errSQL is ${errSQL}`);
            });
          }
        } catch (err) {
          let code = (err as BusinessError).code;
          let message = (err as BusinessError).message;
          console.error(`Register observer failed, code is ${code},message is ${message}`);
        }
        this.promptAction.showToast({ message: `数据库初始化成功.` });
        console.info('initRdb successfully.');
      }).catch((err: BusinessError) => {
        console.error(`initRdb failed, code is ${err.code},message is ${err.message}`);
      });
    } catch (err) {
      console.error(`initRdb failed, code is ${err.code},message is ${err.message}`);
    }
  }

  queryData() {
    if (!this.store) {
      console.error('RdbStore is undefined.');
      return;
    }
    try {
      // 查询数据
      let resultSet = this.store.querySqlSync(`SELECT * FROM ${this.tableName} limit 10`);
      console.info(`ResultSet column names: ${resultSet.columnNames}, row count: ${resultSet.rowCount}`);
      if (resultSet.rowCount > 0) {
        resultSet.getRows(resultSet.rowCount).then((rows: Array<relationalStore.ValuesBucket>) => {
          console.info(`querySqlSync successful rows = ${JSON.stringify(rows)}`);
          this.promptAction.showToast({ message: `查询数据库成功,查询结果：${JSON.stringify(rows)}` });
        }).catch((err: BusinessError) => {
          console.error(`querySqlSync failed, code is ${err.code},message is ${err.message}`);
        }).finally(() => {
          resultSet.close();
        });
      } else {
        resultSet.close();
      }
    } catch (error) {
      let err: BusinessError = error as BusinessError;
      console.error(`queryData failed, code is ${err.code},message is ${err.message}`);
    }
  }
}
```
