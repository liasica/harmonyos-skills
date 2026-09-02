---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-lite-framework-js-file
title: app.js
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > JS组件 > 兼容JS的类Web开发范式（ArkUI.Lite） > 框架说明 > app.js
category: harmonyos-references
scraped_at: 2026-09-02T15:01:13+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:3c5e6d3d3fae26303a71bd988fb0b6f4cf114a5aac0a9e5e80a17ccaa7c19836
---

app.js用于定义应用级生命周期函数和应用全局数据对象，可在应用创建、销毁等阶段执行初始化或资源释放逻辑，并支持在不同页面间共享全局数据，适用于需要统一管理应用状态和生命周期处理的场景。

## 应用生命周期4+

每个应用可以在app.js中自定义应用级生命周期的实现逻辑，包括：

* onCreate：在应用生成时被调用的生命周期函数。
* onDestroy：在应用销毁时被调用的生命周期函数。

以下示例仅在生命周期函数中打印对应日志：

```js
// app.js
export default {
  onCreate() {
    console.info('Application onCreate');
  },
  onDestroy() {
    console.info('Application onDestroy');
  },
};
```

## 应用对象10+

| 属性 | 类型 | 描述 |
| --- | --- | --- |
| getApp | Function | 提供getApp()全局方法，可以在页面JS文件中获取app.js中暴露的数据对象。为兼容不支持getApp的低版本，使用getApp前应先判断其是否可用。 |

**说明** 

应用对象是全局数据，其在整个应用消亡之前都会一直占用JS内存。尽管应用对象可为不同页面共享数据提供便利，但小型设备的可用内存通常受限，应谨慎使用。如果在应用对象中保存过多数据或占用内存较大的数据，则应用进入包含较多组件或资源的page页面时，可能因内存不足而出现异常。

示例如下：

在app.js中声明应用对象。

```javascript
// app.js
export default {
    data: {
        name: 'by getApp'
    },
    onCreate() {
        console.info('Application onCreate');
    },
    onDestroy() {
        console.info('Application onDestroy');
    },
};
```

在具体的页面中访问应用对象。

```javascript
// index.js
export default {
    data: {
        title: ''
    },
    onInit() {
        if (typeof getApp !== 'undefined') {
            var appData = getApp().data;
            if (typeof appData !== 'undefined') {
                this.title = appData.name; // read from app data
            }
        }
    },
    clickHandler() {
        if (typeof getApp !== 'undefined') {
            var appData = getApp().data;
            if (typeof appData !== 'undefined') {
                appData.name = this.title; // write to app data
            }
        }
    }
};
```

**说明** 

为了应用可在不支持getApp的低版本上正常运行，代码中应进行兼容性处理，即在使用getApp前先判断其是否可用。
