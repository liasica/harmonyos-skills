---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-avoid-overusing-custom-component-check
title: "@performance/avoid-overusing-custom-component-check"
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 性能规则@performance > @performance/avoid-overusing-custom-component-check
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:52+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:2635b2f9e5e51a74f2bd07c56f69207e8dbbab65ef0c1616f15a91e872ae2d97
---

当在应用中使用自定义组件时，可以优先使用@Builder函数代替自定义组件，@Builder函数不会在后端FrameNode节点树上创建一个新的树节点，有助于缩短页面的加载和渲染时长。

## 规则配置

```screen
// code-linter.json5
{
  "rules": {
    "@performance/avoid-overusing-custom-component-check": "warn",
  }
}
```

## 选项

该规则无需配置选项。

## 正例

```screen
// 1. 自定义@Builder函数组件
@Builder
function UserCardBuilder(name: string, age?: number, avatarImage?: ResourceStr) {
  Row() {
    Row() {
      Image(avatarImage)
        .size({ width: 50, height: 50 })
        .borderRadius(25)
        .margin(8)
      Text(name)
        .fontSize(30)
    }

    Text(`年龄：${age?.toString()}`)
      .fontSize(20)
  }
  .backgroundColor(DEFAULT_BACKGROUND_COLOR)
  .justifyContent(FlexAlign.SpaceBetween)
  .borderRadius(8)
  .padding(8)
  .height(66)
  .width('80%')
}

@Component
export struct UserCardList {
  @State users: User[] = getUsers();

  aboutToAppear(): void {
    let message = 'hello world';
  }

  build() {
    List({ space: 8 }) {
      ForEach(this.users, (item: User) => {
        ListItem() {
          // 2. 使用@Builder函数
          UserCardBuilder(item.name, item.age, item.avatarImage)
        }
      }, (item: User) => item.id)
    }
    .alignListItem(ListItemAlign.Center)
  }
}
```

## 反例

```screen
import { util } from '@kit.ArkTS';

interface User {
  id: string;
  name: string;
  age?: number;
  avatarImage?: ResourceStr;
  // introduction: string;
  // ...
}

// 构造数据
const DEFAULT_BACKGROUND_COLOR = Color.Pink;
const getUsers = () => {
  const USERS: User[] = [{
    id: '1',
    name: '张三',
  }, {
    id: '2',
    name: '李四',
  }, {
    id: '3',
    name: '王五',
  }];
  return Array.from(Array(30), (item: User, i: number) => {
    return {
      id: util.generateRandomUUID(),
      name: USERS[i%3].name,
      avatarImage: $r('app.media.avatar'),
      age: 18 + i
    } as User;
  });
}

// 用户卡片列表组件
@Component
export struct UserCardList {
  @State users: User[] = getUsers();

  build() {
    List({ space: 8 }) {
      ForEach(this.users, (item: User) => {
        ListItem() {
          UserCard({ name: item.name, age: item.age, avatarImage: item.avatarImage })
        }
      }, (item: User) => item.id)
    }
    .alignListItem(ListItemAlign.Center)
  }
}

// 用户卡片自定义组件
@Component
struct UserCard {
  @Prop avatarImage: ResourceStr;
  @Prop name: string;
  @Prop age: number;

  build() {
    Row() {
      Row() {
        Image(this.avatarImage)
          .size({ width: 50, height: 50 })
          .borderRadius(25)
          .margin(8)
        Text(this.name)
          .fontSize(30)
      }

      Text(`年龄：${this.age.toString()}`)
        .fontSize(20)
    }
    .backgroundColor(DEFAULT_BACKGROUND_COLOR)
    .justifyContent(FlexAlign.SpaceBetween)
    .borderRadius(8)
    .padding(8)
    .height(66)
    .width('80%')
  }
}
```

## 规则集

```screen
plugin:@performance/recommended
plugin:@performance/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
