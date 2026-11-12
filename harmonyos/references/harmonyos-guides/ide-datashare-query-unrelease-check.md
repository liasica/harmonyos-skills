---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-datashare-query-unrelease-check
title: "@performance/datashare-query-unrelease-check"
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 性能规则@performance > @performance/datashare-query-unrelease-check
category: harmonyos-guides
scraped_at: 2026-11-12T09:52:57+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:d726c4b4592fd913e3fc7378a2a3413a64cf5f590a52ee84a2626673292927aa
---

使用DataShareHelper的query接口查询数据后必须及时关闭结果集，以防止内存泄漏。

## 规则配置

```screen
// code-linter.json5
{
  "rules": {
    "@performance/datashare-query-unrelease-check": "warn",
  }
}
```

## 选项

该规则无需配置选项。

## 正例

```screen
import relationalStore from "@ohos.data.relationalStore";
import { AbilityConstant, UIAbility, Want } from "@kit.AbilityKit";
import { BusinessError } from "@kit.BasicServicesKit";
import { window } from "@kit.ArkUI";

let store: relationalStore.RdbStore | undefined;
const STORE_CONFIG: relationalStore.StoreConfig = {
  name: 'rdbtest.db',
  securityLevel: relationalStore.SecurityLevel.S3
}

export class DataShareQueryUnReleaseNoReport0 extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
    relationalStore.getRdbStore(this.context, STORE_CONFIG,
      (err: BusinessError, rdbStore: relationalStore.RdbStore) => {
        store = rdbStore;
      });
  }

  onWindowStageCreate(windowStage: window.WindowStage): void {
    if (store) {
      this.query_1_query_callback();
    }
  }

  private query_1_query_callback(): void {
    let predicates = new relationalStore.RdbPredicates('EMPLOYEE');
    predicates.equalTo('NAME', 'JACK');
    (store as relationalStore.RdbStore).query(predicates, (err, resultSet) => {
      if (err) {
        return;
      }
      while (resultSet.goToNextRow()) {
        const id = resultSet.getLong(resultSet.getColumnIndex('ID'));
        const name = resultSet.getLong(resultSet.getColumnIndex('NAME'));
        const age = resultSet.getLong(resultSet.getColumnIndex('AGE'));
        const gender = resultSet.getLong(resultSet.getColumnIndex('GENDER'));
      }
      resultSet.close();
    });
  }
}
```

## 反例

```screen
import relationalStore from "@ohos.data.relationalStore";
import { AbilityConstant, UIAbility, Want } from "@kit.AbilityKit";
import { BusinessError } from "@kit.BasicServicesKit";
import { window } from "@kit.ArkUI";

let store: relationalStore.RdbStore | undefined;
const STORE_CONFIG: relationalStore.StoreConfig = {
  name: 'rdbtest.db',
  securityLevel: relationalStore.SecurityLevel.S3
}

export class DataShareQueryUnReleaseReport0 extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
    relationalStore.getRdbStore(this.context, STORE_CONFIG,
      (err: BusinessError, rdbStore: relationalStore.RdbStore) => {
        store = rdbStore;
      });
  }

  onWindowStageCreate(windowStage: window.WindowStage): void {
    if (store) {
      this.query_1_query_callback();
    }
  }

  private query_1_query_callback(): void {
    let predicates = new relationalStore.RdbPredicates('EMPLOYEE');
    predicates.equalTo('NAME', 'JACK');
    //告警
    (store as relationalStore.RdbStore).query(predicates, (err, resultSet) => {
      if (err) {
        return;
      }
      while (resultSet.goToNextRow()) {
        const id = resultSet.getLong(resultSet.getColumnIndex('ID'));
        const name = resultSet.getLong(resultSet.getColumnIndex('NAME'));
        const age = resultSet.getLong(resultSet.getColumnIndex('AGE'));
        const gender = resultSet.getLong(resultSet.getColumnIndex('GENDER'));
      }
    });
  }
}
```

## 规则集

```screen
plugin:@performance/recommended
plugin:@performance/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查（ArkTS/TS）](ide-code-linter.md)。
