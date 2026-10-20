---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/arkdata-kit-troubleshooting-0001
title: 数据库句柄资源过载异常问题排查与解决
breadcrumb: FAQ > 应用框架开发 > 本地数据和文件 > 本地数据库管理 > 故障排查 > 数据库句柄资源过载异常问题排查与解决
category: harmonyos-faqs
scraped_at: 2026-10-21T07:11:40+08:00
doc_updated_at: 2026-10-20
content_hash: sha256:45ecf6e431c118852eee2e1141d0ef146cf4f06b811b60f3bef51425dba506c8
---

## 问题现象

跑稳定性测试过程中，抛出了“稳定性：应用在运行中出现文件句柄资源过载异常的问题”，该如何解决呢？详情日志如下：

```txt
fd of process painless.xiangzi.tech exceeds: 5158
top10:
2519 /data/storage/el2/database/entry/rdb/encrypt_dict_v1.db
2519 /data/storage/el2/database/entry/rdb/encrypt_dict_v1.db-wal
......
```

## 定位过程

数据库出现句柄资源过载常见原因一般有两点：

* 数据库资源没有及时释放。
* 开启了事务，事务没有及时提交或者回滚。

需要检查数据库资源是否及时释放、开启了事务之后事务是否及时提交或者回滚。

## 分析结论

在操作数据库时，频繁获取数据库操作对象relationalStore.RdbStore，处理完业务后，该对象没有及时关闭，导致句柄累积过多，最终产生句柄资源过载异常。

## 修改建议

基于分析结论，提供以下两种修改方案：

* 方案一：及时释放掉RdbStore，代码示例如下：

  ```ts
  import { Context } from '@kit.AbilityKit';
  import { relationalStore } from '@kit.ArkData';

  export interface Employee {
    id?: number,
    name: string
  }

  export class EmployeeDbModel {

    private context: Context;
    private readonly TABLE_NAME = 'Employee';
    private readonly STORE_CONFIG: relationalStore.StoreConfig = {
      name: 'RdbTest.db',
      securityLevel: relationalStore.SecurityLevel.S1
    };

    constructor(context: Context) {
      this.context = context;
    }

    createTable() {
      const createTableSql: string = `
        CREATE TABLE IF NOT EXISTS Employee (
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          name TEXT NOT NULL
        )`;
      this.dbHandlerVoid((db: relationalStore.RdbStore) => {
        try {
          db.executeSync(createTableSql);
        } catch (error) {
          console.error(JSON.stringify(error));
        }
      });
    }

    async insert(emp: Employee) {
      await this.dbHandlerVoid(db => {
        db.insert(this.TABLE_NAME, {
          name: emp.name
        }).catch(() => {
          console.error('插入数据异常');
        });
      });
    }

    async query() {
      let emps = await this.dbHandlerReturn(db => {
        let emps: Employee[] = [];
        try {
          let predicates = new relationalStore.RdbPredicates(this.TABLE_NAME);
          let resultSet = db.querySync(predicates);
          while (resultSet.goToNextRow()) {
            emps.push({
              id: resultSet.getLong(resultSet.getColumnIndex('id')),
              name: resultSet.getString(resultSet.getColumnIndex('name'))
            });
          }
        } catch (error) {
          console.error(JSON.stringify(error));
        }
        return emps;
      }) as Employee[];
      return emps;
    }

    async dbHandlerVoid(handler: (db: relationalStore.RdbStore) => void): Promise<void> {
      let db: relationalStore.RdbStore | null = null;
      try {
        db = await relationalStore.getRdbStore(this.context, this.STORE_CONFIG);
        handler(db);
      } catch (err) {
        console.error('操作失败:', err);
      } finally {
        if (db) {
          db.close().catch(() => {
            console.error('关闭数据库异常！');
          });
        }
      }
    }

    async dbHandlerReturn(handler: (db: relationalStore.RdbStore) => Object[]): Promise<Object[] | undefined> {
      let db: relationalStore.RdbStore | null = null;
      try {
        db = await relationalStore.getRdbStore(this.context, this.STORE_CONFIG);
        return handler(db);
      } catch (err) {
        console.error('操作失败:', err);
      } finally {
        if (db) {
          db.close().catch(() => {
            console.error('关闭数据库异常！');
          });
        }
      }
      return [];
    }

  }
  ```
* 方案二：全局唯一数据库实例RdbStore，避免多次创建。使用前建议在EntryAbility中onCreate生命周期回调方法中进行初始化DatabaseManager.init(this.context)。代码示例参考如下：

  ```ts
  import { Context } from '@kit.AbilityKit';
  import { relationalStore } from '@kit.ArkData';

  export class DatabaseManager {
    private static instance: relationalStore.RdbStore | null = null;
    private static context: Context;

    static init(context: Context) {
      DatabaseManager.context = context;
    }

    static async getInstance() {
      if (!DatabaseManager.instance) {
        let config: relationalStore.StoreConfig = {
          name: 'RdbTest.db',
          securityLevel: relationalStore.SecurityLevel.S1
        };
        DatabaseManager.instance = await relationalStore.getRdbStore(DatabaseManager.context, config);
      }
      return DatabaseManager.instance;
    }

    static async close() {
      if (DatabaseManager.instance) {
        await DatabaseManager.instance.close();
        DatabaseManager.instance = null;
      }
    }
  }

  export interface Employee {
    id?: number,
    name: string
  }

  export class EmployeeDbModel {
    private readonly TABLE_NAME = 'Employee';

    async createTable() {
      const createTableSql: string = `
        CREATE TABLE IF NOT EXISTS Employee (
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          name TEXT NOT NULL
        )`;
      let rdbStore = await DatabaseManager.getInstance();
      try {
        rdbStore.executeSync(createTableSql);
      } catch (error) {
        console.error(JSON.stringify(error));
      }
    }

    async insert(emp: Employee) {
      let rdbStore = await DatabaseManager.getInstance();
      rdbStore.insert(this.TABLE_NAME, {
        name: emp.name
      }).catch(() => {
        console.error('插入数据异常');
      });
    }

    async query() {
      let emps: Employee[] = [];
      let rdbStore = await DatabaseManager.getInstance();
      let predicates = new relationalStore.RdbPredicates(this.TABLE_NAME);
      try {
        let resultSet = rdbStore.querySync(predicates);
        while (resultSet.goToNextRow()) {
          emps.push({
            id: resultSet.getLong(resultSet.getColumnIndex('id')),
            name: resultSet.getString(resultSet.getColumnIndex('name'))
          });
        }
      } catch (error) {
        console.error(JSON.stringify(error));
      }
      return emps;
    }

  }
  ```

  测试页面代码如下（如果上文中的EmployeeDbModel、Employee和该测试页面没有定义在同一个文件当中，则需要先导入这两个类。另外方案一可直接使用该测试页面；方案二需修改成员对象empDbModel，修改为empDbModel: EmployeeDbModel = new EmployeeDbModel();）：

  ```ts
  @Entry
  @Component
  struct Index {
    empDbModel: EmployeeDbModel = new EmployeeDbModel(this.getUIContext().getHostContext()!);
    @State emps: Employee[] = [];

    aboutToAppear(): void {
      this.empDbModel.createTable();
    }

    build() {
      Column({space: 30}) {
        Button('插入')
          .onClick(() => {
            this.empDbModel.insert({
              name: '小明'
            });
            this.empDbModel.insert({
              name: '小红'
            });
          })

        Button('查询')
          .onClick(async () => {
            this.emps = await this.empDbModel.query();
          })

        Column() {
          ForEach(this.emps, (emp: Employee) => {
            Row() {
              Text(`${emp.id} --- ${emp.name}`)
            }
          })
        }
        .width('100%')
      }
      .height('100%')
      .width('100%')
      .justifyContent(FlexAlign.Center)
    }
  }
  ```
