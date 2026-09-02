---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkweb-140
title: Web组件频繁改变高度卡顿
breadcrumb: FAQ > 应用框架开发 > Web框架 > Web开发（ArkWeb） > Web组件频繁改变高度卡顿
category: harmonyos-faqs
scraped_at: 2026-09-02T15:04:10+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:5ffb4311e5647419242b7b3d8450468bc477b4f25cba296c888a46c0fd34ca43
---

## 问题现象

频繁调整Web组件的高度导致卡顿？

## 背景知识

[onScaleChange](../harmonyos-references/arkts-basic-components-web-events.md#onscalechange9)：当前页面显示比例的变化时触发该回调。

## 解决方案

* 由于高度更新过于频繁，触发了不必要的重渲染或布局计算。
* 可以使用节流或防抖来限制更新频率，减少性能消耗。

ArkTS代码如下：

```ts
import { webview } from '@kit.ArkWeb';

@Component
struct Demo {
  public controller: webview.WebviewController = new webview.WebviewController();
  changeEvent: (event: OnScaleChangeEvent) => void = () => {
  };

  build() {
    Web({
      src: $rawfile('webScaleChange.html'),
      controller: this.controller
    })
      .zoomAccess(true)
      .fileAccess(false)
      .geolocationAccess(false)
      .onScaleChange((event) => {
        this.changeEvent(event);
      })
      .horizontalScrollBarAccess(false)
      .verticalScrollBarAccess(false);
  }
}

class Util {
  // 防抖，在一段时间内函数被多次触发，防抖让函数在一段时间内只执行一次
  static debounce(fun: (height: number) => void, delay?: number) {
    let timer: number;
    return (height: number) => {
      clearTimeout(timer);
      timer = setTimeout(() => {
        fun(height);
      }, delay ? delay : 300);
    };
  }
}

@Entry
@Component
struct Index {
  @State webHeight: number = 600; // 当前显示高度
  constWebHeight: number = 600; // 基础计算高度
  originScale: number = 100; // 初始比例
  webController: webview.WebviewController = new webview.WebviewController();
  // 创建防抖函数实例（300ms延迟）
  debouncedSetHeight: (height: number) => void = Util.debounce((newHeight: number) => {
    this.webHeight = newHeight;
    console.info(`防抖后高度：${this.webHeight}`);
  }, 300);

  build() {
    Column() {
      Demo({
        controller: this.webController,
        changeEvent: (event: OnScaleChangeEvent) => {
          const targetHeight = this.constWebHeight * event.newScale / this.originScale;
          this.debouncedSetHeight(targetHeight); // 此处触发防抖函数，替换成this.webHeight = targetHeight则表示不采用防抖函数
        }
      });
    }
    .height(this.webHeight)
    .width('100%');
  }
}
```

html代码如下：

```html
<!DOCTYPE html>
<html lang="zh">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>复杂页面示例</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
<header>
    <nav>
        <ul>
            <li><a href="#home">首页</a></li>
            <li><a href="#news">新闻</a></li>
            <li><a href="#contact">联系我们</a></li>
            <li><a href="#about">关于我们</a></li>
        </ul>
    </nav>
</header>
<main>
    <section id="home">
        <h1>欢迎来到我们的网站</h1>
        <p>这是一个示例页面，展示了如何创建一个复杂的HTML页面。</p>
    </section>
    <section id="news">
        <h2>最新新闻</h2>
        <article>
            <h3>新闻标题</h3>
            <p>这里是新闻的详细内容。</p>
        </article>
    </section>
    <aside>
        <h2>侧边栏</h2>
        <p>这里是一些额外的信息或者广告。</p>
    </aside>
</main>
<footer>
    <p>© 2023 公司名称. 保留所有权利。</p>
</footer>
<script src="script.js"></script>
</body>
</html>

<style>

    body {
        font-family: Arial, sans-serif;
        margin: 0;
        padding: 0;
    }
    header {
        background: #333;
        color: #fff;
        padding: 10px 0;
    }
    nav ul {
        list-style: none;
        padding: 0;
    }
    nav ul li {
        display: inline;
        margin-right: 10px;
    }
    nav ul li a {
        color: #fff;
        text-decoration: none;
    }
    main {
        display: flex; /* 使用Flexbox布局 */
    }
    section, aside {
        padding: 20px;
    }
    section#home {
        flex: 3; /* 主内容区域占据更多空间 */
    }
    aside {
        flex: 1; /* 侧边栏占据较少空间 */
        background: #f4f4f4;
    }
    footer {
        text-align: center;
        padding: 10px 0;
        background: #333;
        color: #fff;
    }
</style>
```

可以通过双指捏动手机屏幕来实现页面的放大和缩小，对比观察是否采用防抖函数时的现象差。

**说明** 

防抖函数设置的时延delay指的是改变Column组件高度webHeight的间隔时间。

## 常见FAQ

Q：使用Web组件页面时，在网页加载过程中，页面底部可能出现闪烁现象。

A：应用可以通过设置与网页背景色相同的Web组件的背景色，避免视觉闪烁。请参阅[闪烁原因](../harmonyos-guides/web-router-flash-optimization.md#闪烁原因)和[优化方法](../harmonyos-guides/web-router-flash-optimization.md#优化方法)了解详情。
