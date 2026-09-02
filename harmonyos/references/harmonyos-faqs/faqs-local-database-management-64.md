---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-local-database-management-64
title: 如何通过关系型数据库实现全文检索
breadcrumb: FAQ > 应用框架开发 > 本地数据和文件 > 本地数据库管理 > 如何通过关系型数据库实现全文检索
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:29+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:0a82d5bd5832b2f30166433bd215f55c56b009cec1b6cd3a785599def3af390f
---

## 问题现象

官方提供的关系型数据库是否支持fts全文检索？具体应该如何实现。

## 背景知识

* 全文检索（Full-Text Search）是一种高效的文本搜索技术，它通过扫描文档中的每一个词，对每个词建立索引，指明该词在文档中出现的次数和位置。当用户查询时，检索程序根据事先建立的索引进行查找。
* [关系型数据库（Relational Database，RDB）](../harmonyos-references/arkts-apis-data-relationalstore.md)是一种基于关系模型来管理数据的数据库。关系型数据库基于SQLite组件提供了一套完整的对本地数据库进行管理的机制，对外提供了一系列的增、删、改、查等接口，也可以直接运行用户输入的SQL语句来满足复杂的场景需要。
* 创建关系型数据库时可以通过[StoreConfig](../harmonyos-references/arkts-apis-data-relationalstore-i.md#storeconfig)管理数据库相关配置，其中[Tokenizer](../harmonyos-references/arkts-apis-data-relationalstore-e.md#tokenizer17)可用于指定用户在fts场景下使用哪种分词器。当此参数不填时，则在fts下不支持中文以及多国语言分词，但仍可支持英文分词。如果用户想使用自定义分词器，可以通过pluginLibs参数进行配置，具体请见[pluginLibs的使用约束和示例](../harmonyos-references/arkts-apis-data-relationalstore-i.md#pluginlibs的使用约束和示例)。

## 解决方案

关系型数据库没有提供直接的接口设置全文检索，需要在建表时执行SQL语句CREATE VIRTUAL TABLE语句建立FTS表，再使用MATCH操作符实现检索。

| 分词功能 | StoreConfig配置 | 建表语句示例 |
| --- | --- | --- |
| 不使用icu分词，仅使用英文分词 | tokenizer设为NONE\_TOKENIZER或不设置该字段 | CREATE VIRTUAL TABLE example USING fts4(name, content, tokenize=unicode61) |
| 使用icu分词器 | tokenizer设为ICU\_TOKENIZER | CREATE VIRTUAL TABLE example USING fts4(name, content, tokenize=icu zh\_CN) |
| 使用自研分词器 | tokenizer设为CUSTOM\_TOKENIZER | CREATE VIRTUAL TABLE example USING fts5(name, content, tokenize=customtokenizer) |
| 使用自定义分词器 | 不设置tokenizer字段，配置pluginLibs字段 | CREATE VIRTUAL TABLE example USING fts5(name, content, tokenize=自定义分词器名称) |

* 不使用icu分词功能，仅使用英文分词。

  创建数据库时tokenizer设为NONE\_TOKENIZER或不设置该字段，建表时指定英文分词器类型（如：tokenize=unicode61），查询时使用MACTH关键字做全文检索。

  ```ts
  dbConfig1: relationalStore.StoreConfig = {
    name: 'fts_test1.db',
    securityLevel: relationalStore.SecurityLevel.S1
    // tokenizer设为NONE_TOKENIZER或不设置该字段，仅可使用默认英文分词器
  };
  createTableSql1: string =
    `CREATE VIRTUAL TABLE IF NOT EXISTS ${this.tableName} USING fts4(title, authors, content, tokenize=unicode61)`;
  ```

  ```ts
  // 查询sql使用MATCH全文检索
  querySql: string = `SELECT DISTINCT * FROM ${this.tableName} WHERE content MATCH ?;`;
  ```
* 使用icu分词器，支持中文以及多国语言。指定icu分词器时，可指定使用哪种语言，例如zh\_CN表示中文，tr\_TR表示土耳其语等。详细支持的语言种类，请查阅[ICU分词器](https://gitcode.com/openharmony/third_party_icu/blob/master/icu4c/source/data/lang/zh.txt)。详细的语言缩写，请查阅该目录（[ICU支持的语言缩写](https://gitcode.com/openharmony/third_party_icu/tree/master/icu4c/source/data/locales)）下的文件名。

  创建数据库时tokenizer设为ICU\_TOKENIZER，建表时指定分词器类型（如：tokenize=icu zh\_CN），查询时使用MACTH关键字做全文检索。

  ```ts
  dbConfig2: relationalStore.StoreConfig = {
    name: 'fts_test2.db',
    securityLevel: relationalStore.SecurityLevel.S1,
    // 配置tokenizer为ICU_TOKENIZER，启用icu分词器
    tokenizer: relationalStore.Tokenizer.ICU_TOKENIZER
  };
  createTableSql2: string =
    `CREATE VIRTUAL TABLE IF NOT EXISTS ${this.tableName} USING fts4(title, authors, content, tokenize=icu zh_CN)`;
  ```

  ```ts
  // 查询sql使用MATCH全文检索
  querySql: string = `SELECT DISTINCT * FROM ${this.tableName} WHERE content MATCH ?;`;
  ```
* 使用自研分词器，可支持中文（简体、繁体）、英文、阿拉伯数字。CUSTOM\_TOKENIZER相比ICU\_TOKENIZER在分词准确率、常驻内存占用上更有优势。自研分词器支持默认分词模式和短词分词模式（short\_words）两种，使用参数cut\_mode可指定模式，不指定模式时使用默认模式。

  创建数据库时tokenizer设为CUSTOM\_TOKENIZER，建表时指定分词器类型（如：tokenize=customtokenizer），查询时使用MACTH关键字做全文检索。

  ```ts
  dbConfig3: relationalStore.StoreConfig = {
    name: 'fts_test3.db',
    securityLevel: relationalStore.SecurityLevel.S1,
    // 配置tokenizer为CUSTOM_TOKENIZER，启用自研分词器
    tokenizer: relationalStore.Tokenizer.CUSTOM_TOKENIZER
  };
  createTableSql3: string =
    `CREATE VIRTUAL TABLE IF NOT EXISTS ${this.tableName} USING fts5(title, authors, content, tokenize=customtokenizer)`;
  ```

  ```ts
  // 查询sql使用MATCH全文检索
  querySql: string = `SELECT DISTINCT * FROM ${this.tableName} WHERE content MATCH ?;`;
  ```
* 若想使用自定义分词器，可以通过pluginLibs参数进行配置，具体请见[pluginLibs的使用约束和示例](../harmonyos-references/arkts-apis-data-relationalstore-i.md#pluginlibs的使用约束和示例)。

使用英文分词、icu分词器、自研分词器使用可参考如下示例代码：

```ts
import { relationalStore, ValuesBucket } from '@kit.ArkData';
import { common } from '@kit.AbilityKit';

// 预置数据
const DATA_LIST: ValuesBucket[] = [
  { 'title': '静夜思', 'authors': '李白', 'content': '床前明月光，疑是地上霜。\n举头望明月，低头思故乡。' },
  { 'title': '竹里馆', 'authors': '王维', 'content': '独坐幽篁里，弹琴复长啸。\n深林人不知，明月来相照。' },
  { 'title': '近代吴歌·秋歌', 'authors': '鲍令晖', 'content': '秋风入窗里，罗帐起飘飏。\n仰头看明月，寄情千里光。' },
  { 'title': '渌水曲', 'authors': '李白', 'content': '渌水明秋月，南湖采白蘋。\n荷花娇欲语，愁杀荡舟人。' },
  {
    'title': 'The Moon',
    'authors': 'R. L. Stevenson',
    'content': 'The moon has a face like the clock in the hall;\n' +
      'She shines on thieves on the garden wall,\n' +
      'On streets and fields and harbour quays,\n' +
      'And birdies asleep in the forks of the trees.'
  },
  {
    'title': 'Song to the Moon',
    'authors': 'Antonín Leopold Dvořák',
    'content': 'O Moon, high in the heavens, silver bright,\n' +
      'You wander through the starry night.\n' +
      'Tell me, where is my beloved one?\n' +
      'Tell me, Moon, where has he gone?'
  },
  {
    'title': 'Had I not seen the Sun',
    'authors': 'Emily Dickinson',
    'content': 'Had I not seen the Sun,\n' +
      'I could have borne the shade.\n' +
      'But Light a newer Wilderness,\n' +
      'My Wilderness has made.'
  },
];

@Entry
@Component
struct RdbFtsDemo {
  @State currentIndex: number = 0;
  @State selectedIndex: number = 0;
  @State results: Array<relationalStore.ValuesBucket> = [];
  store: relationalStore.RdbStore | undefined = undefined;
  context = this.getUIContext().getHostContext() as common.UIAbilityContext;
  promptAction = this.getUIContext().getPromptAction();
  tableName: string = 'fts_table';
  dbConfig1: relationalStore.StoreConfig = {
    name: 'fts_test1.db',
    securityLevel: relationalStore.SecurityLevel.S1
    // tokenizer设为NONE_TOKENIZER或不设置该字段，仅可使用默认英文分词器
  };
  createTableSql1: string =
    `CREATE VIRTUAL TABLE IF NOT EXISTS ${this.tableName} USING fts4(title, authors, content, tokenize=unicode61)`;

  dbConfig2: relationalStore.StoreConfig = {
    name: 'fts_test2.db',
    securityLevel: relationalStore.SecurityLevel.S1,
    // 配置tokenizer为ICU_TOKENIZER，启用icu分词器
    tokenizer: relationalStore.Tokenizer.ICU_TOKENIZER
  };
  createTableSql2: string =
    `CREATE VIRTUAL TABLE IF NOT EXISTS ${this.tableName} USING fts4(title, authors, content, tokenize=icu zh_CN)`;

  dbConfig3: relationalStore.StoreConfig = {
    name: 'fts_test3.db',
    securityLevel: relationalStore.SecurityLevel.S1,
    // 配置tokenizer为CUSTOM_TOKENIZER，启用自研分词器
    tokenizer: relationalStore.Tokenizer.CUSTOM_TOKENIZER
  };
  createTableSql3: string =
    `CREATE VIRTUAL TABLE IF NOT EXISTS ${this.tableName} USING fts5(title, authors, content, tokenize=customtokenizer)`;

  // 查询sql使用MATCH全文检索
  querySql: string = `SELECT DISTINCT * FROM ${this.tableName} WHERE content MATCH ?;`;

  build() {
    Column({ space: 20 }) {

      Tabs() {
        TabContent() {
          this.buttons();
        }.tabBar(this.tabBuilder(0, '英文分词'));

        TabContent() {
          this.buttons();
        }.tabBar(this.tabBuilder(1, 'icu中文分词'));

        TabContent() {
          this.buttons();
        }.tabBar(this.tabBuilder(2, 'icu自研分词器'));
      }
      .barMode(BarMode.Fixed)
      .onChange((index: number) => {
        this.currentIndex = index;
      })
      .onSelected((index: number) => {
        this.selectedIndex = index;
        this.results = [];
        this.deleteRdb();
      });
    }
    .justifyContent(FlexAlign.Center)
    .height('100%')
    .width('100%');
  }

  @Builder
  tabBuilder(index: number, name: string) {
    Column() {
      Text(name)
        .fontColor(this.selectedIndex === index ? '#0A59F7' : '#000000')
        .fontSize(16)
        .fontWeight(this.selectedIndex === index ? 500 : 400)
        .lineHeight(22)
        .margin({ top: 17, bottom: 7 });
      Divider()
        .strokeWidth(2)
        .color('#0A59F7')
        .opacity(this.selectedIndex === index ? 1 : 0);
    }.width('100%');
  }

  @Builder
  buttons() {
    Column({ space: 20 }) {

      ForEach(this.results, (data: relationalStore.ValuesBucket) => {
        TextArea({
          text: `${data['title'] as string}(${data['authors'] as string})\n\n${data['content'] as string}`
        })
          .backgroundColor('#D1D1D6')
          .fontSize(15)
          .margin({ left: 20, right: 20 });
      });

      Button('初始化fts表数据')
        .onClick(() => {
          this.initRdb();
        });

      Button('查询数据')
        .onClick(() => {
          this.queryData();
        });
    };
  }

  initRdb() {
    // 1.创建数据库实例
    let dbConfig = this.getDbConfig();
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
      console.info('initRdb successfully.');
      // 2.创建fts表
      this.createTable().then(() => {
        // 3.预置表数据
        this.insertData();
        this.promptAction.showToast({ message: `初始化成功` });
      });
    })
      .catch((err: BusinessError) => {
        console.error(`initRdb failed, code is ${err.code},message is ${err.message}`);
      });
  }

  async createTable() {
    try {
      if (this.store) {
        let createSql = this.createTableSql1;
        switch (this.currentIndex) {
          case 1:
            createSql = this.createTableSql2;
            break;
          case 2:
            createSql = this.createTableSql3;
            break;
          default:
            createSql = this.createTableSql1;
            break;
        }
        await this.store.executeSql(createSql);
        console.info(`executeSql successful. 创建fts表成功`);
      }
    } catch (err) {
      let code = (err as BusinessError).code;
      let message = (err as BusinessError).message;
      console.error(`createTableAndInsertData failed, code is ${code},message is ${message}`);
    }
  }

  insertData() {
    try {
      if (this.store) {
        let insertName = this.store.batchInsertSync(this.tableName, DATA_LIST);
        console.info(`batchInsertSync successful. insertName= ${insertName}`);
      }
    } catch (err) {
      let code = (err as BusinessError).code;
      let message = (err as BusinessError).message;
      console.error(`batchInsertSync failed, code is ${code},message is ${message}`);
    }
  }

  queryData() {
    try {
      if (this.store) {
        let keywords = 'sun';
        switch (this.currentIndex) {
          case 1:
          case 2:
            keywords = '明月';
            break;
          default:
            keywords = 'moon';
            break;
        }
        let resultSet = this.store.querySqlSync(this.querySql, [keywords]);
        console.info(`ResultSet column names: ${resultSet.columnNames}, row count: ${resultSet.rowCount}`);
        let rows: Array<relationalStore.ValuesBucket> = [];
        while (resultSet.goToNextRow()) {
          let row: relationalStore.ValuesBucket = resultSet.getRow();
          rows.push(row);
        }
        // 释放数据集的内存
        resultSet.close();
        if (rows && rows.length > 0) {
          this.results = rows;
        }
        console.info(`RelationalStoreDemo remoteQuery rows= ${JSON.stringify(rows)}`);
      }
    } catch (err) {
      let code = (err as BusinessError).code;
      let message = (err as BusinessError).message;
      console.error(`querySqlSync failed, code is ${code},message is ${message}`);
    }
  }

  getDbConfig() {
    let dbConfig = this.dbConfig1;
    switch (this.currentIndex) {
      case 1:
        dbConfig = this.dbConfig2;
        break;
      case 2:
        dbConfig = this.dbConfig3;
        break;
      default:
        dbConfig = this.dbConfig1;
        break;
    }
    return dbConfig;
  }

  deleteRdb() {
    if (this.store) {
      let dbConfig = this.getDbConfig();
      relationalStore.deleteRdbStore(this.context, dbConfig).then(() => {
        this.store = undefined;
        console.info('deleteRdbStore successfully.');
      })
        .catch((err: BusinessError) => {
          console.error(`deleteRdbStore failed, code is ${err.code},message is ${err.message}`);
        });
    }
  }
}
```

## 常见FAQ

Q：使用官方提供的关系型数据库创建分词器为icu zh\_CN的fts5类型表时报错。

A：[关系型数据库（Relational Database，RDB）](../harmonyos-references/arkts-apis-data-relationalstore.md)基于SQLite组件实现，对全文搜索的支持与SQLite保持一致：[fts5不支持ICU分词器](https://www.sqlite.org/fts5.html#_changes_to_create_virtual_table_statements_)，若需要使用ICU中文分词器请使用fts3/fts4实现或[使用pluginLibs加载开发者自定义分词器](../harmonyos-references/arkts-apis-data-relationalstore-i.md#pluginlibs的使用约束和示例)实现。

Q：关系型数据库创建fts时使用语句CREATE VIRTUAL TABLE IF NOT EXISTS tablename USING fts4(fts\_id UNINDEXED, title, content, tokenize='icu "zh\_CN"')报错tokenize='icu "zh\_CN"'不支持。

A：关系型数据库对SQL语句校验规则与SQLite保持一致，SQLite并不支持该写法，请更改为tokenize=icu "zh\_CN"或tokenize=icu zh\_CN。

Q：关系型数据库是否支持中文分词单字检索？

A：关系型数据库当前提供icu分词器和自研分词器都支持中文分词，但都是基于词条实现分词，不支持中文单字检索。若需要使用中文单字检索，可[使用pluginLibs加载开发者自定义分词器](../harmonyos-references/arkts-apis-data-relationalstore-i.md#pluginlibs的使用约束和示例)实现。

Q：关系型数据库是否支持unicode61分词器，是否支持通过categories指定分词器保留的字符类型？

A：支持，使用如下建表语句可实现：CREATE VIRTUAL TABLE example USING fts5(name, content, tokenize="unicode61 categories 'L\* N\*'")。
