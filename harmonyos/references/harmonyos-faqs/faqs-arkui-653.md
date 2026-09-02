---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-653
title: 参数传递错误导致执行getXComponentSurfaceId出现应用闪退
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 参数传递错误导致执行getXComponentSurfaceId出现应用闪退
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:25+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:b59553b26cf65ab648948e5a637005298ac519bcc76389ac1e1f3e53f5c661e4
---

## 问题现象

创建XComponent后调用getXComponentSurfaceId方法出现Crash异常，并且onSurfaceCreated方法没有被执行，问题代码如下：

```ts
@Entry
@Component
struct Problem {
  @State xcArray: CustomXComponentController[] = [];

  aboutToAppear(): void {
    for (let i = 0; i < 2; i++) {
      this.xcArray.push(new CustomXComponentController());
    }
  }

  build() {
    Column() {
      XScreen({ xcArray: this.xcArray });
    }
    .height('100%')
    .width('100%');
  }
}

@Component
struct XScreen {
  @Prop xcArray: CustomXComponentController[];

  build() {
    Column() {
      ForEach(this.xcArray, (xc: CustomXComponentController, index: number) => {
        Button('ButtonXc:' + index)
          .onClick(() => {
            console.info(`getXComponentSurfaceId = ${xc.getXComponentSurfaceId()}`);
          });
        XComponent({
          id: 'XComponent' + index,
          type: XComponentType.SURFACE,
          controller: xc
        })
          .width('100%')
          .height(200);
      });
    }.width('100%')
    .height('100%');
  }
}

class CustomXComponentController extends XComponentController {
  onSurfaceCreated(surfaceId: string): void {
    console.info(`onSurfaceCreated surfaceId: ${surfaceId}`);
  }

  onSurfaceChanged(surfaceId: string, rect: SurfaceRect): void {
    console.info(`onSurfaceChanged surfaceId: ${surfaceId}, rect: ${JSON.stringify(rect)}}`);
  }

  onSurfaceDestroyed(surfaceId: string): void {
    console.info(`onSurfaceDestroyed surfaceId: ${surfaceId}`);
  }
}
```

Crash日志如下：

```log
Process name:com.example.xxx
Process life time:3s
Reason:Signal:SIGSEGV(SEGV_MAPERR)@0x0000000000000018  probably caused by NULL pointer dereference
Fault thread info:
Tid:29620, Name:250918175335021
#00 pc 0000000000e2c300 /system/lib64/platformsdk/libace_compatible.z.so(OHOS::Ace::Framework::JSXComponentController::GetSurfaceId(OHOS::Ace::Framework::JsiCallbackInfo const&)+8)(eab4f4be93e4c3c88d2272a46b36c765)
#01 pc 0000000000e2ca38 /system/lib64/platformsdk/libace_compatible.z.so(panda::Local<panda::JSValueRef> OHOS::Ace::Framework::JsiClass<OHOS::Ace::Framework::JSXComponentController>::InternalJSMemberFunctionCallback<OHOS::Ace::Framework::JSXComponentController>(panda::JsiRuntimeCallInfo*)+256)(eab4f4be93e4c3c88d2272a46b36c765)
#02 pc 0000000000589f1c /system/lib64/platformsdk/libark_jsruntime.so(panda::Callback::RegisterCallback(panda::ecmascript::EcmaRuntimeCallInfo*)+272)(38230492305256c23dcf27a2aba6f771)
#03 pc 0000000000445a2c /system/lib64/module/arkcompiler/stub.an(RTStub_PushCallArgsAndDispatchNative+40)
#04 at anonymous (entry/src/main/ets/pages/XScreen.ets:22:49)
```

## 背景知识

* [XComponent](../harmonyos-references/ts-basic-components-xcomponent.md)：提供用于图形绘制和媒体数据写入的Surface，XComponent负责将其嵌入到视图中，支持应用自定义Surface位置和大小。
* [getXComponentSurfaceId](../harmonyos-references/ts-basic-components-xcomponent.md#getxcomponentsurfaceid9)：获取XComponent对应Surface的ID，仅XComponent类型为SURFACE("surface")或TEXTURE时有效。

## 问题定位

1. 观察Crash日志probably caused by NULL pointer dereference，发现可能是CustomXComponentController对象为空。
2. 结合onSurfaceCreated方法未执行现象可以推测出XComponent对象未正确创建。
3. 观察XComponent中xcArray来源，发现可能是由于参数传递不正确导致XComponent对象未正确创建。
4. 修改代码，在XScreen页面构造xcArray对象进行尝试：

   ```ts
   aboutToAppear(): void {
       for (let i = 0; i < 2; i++) {
       this.xcArray.push(new CustomXComponentController())
     }
   }
   ```
5. 发现能够正确执行getXComponentSurfaceId方法，故可以得出结论：由于参数传递不正确导致应用闪退。

## 分析结论

@Prop装饰变量时会进行深拷贝，子页面渲染完成后xcArray对象还未传递完成，会导致XComponent对象创建异常，因此使用getXComponentSurfaceId方法出现闪退，具体原理可以参考[@Prop修饰的值没有及时更新如何解决](faqs-arkui-1629.md)。

## 修改建议

* 方案一：xcArray对象在该场景未绑定UI，故不需要使用状态管理参数传递。

  ```ts
  @Entry
  @Component
  struct Solution1 {
    xcArray: CustomXComponentController1[] = [];

    aboutToAppear(): void {
      for (let i = 0; i < 2; i++) {
        this.xcArray.push(new CustomXComponentController1());
      }
    }

    build() {
      Column() {
        XScreen1({ xcArray: this.xcArray });
      }
      .height('100%')
      .width('100%');
    }
  }

  @Component
  struct XScreen1 {
    xcArray: CustomXComponentController1[] = [];

    build() {
      Column() {
        ForEach(this.xcArray, (xc: CustomXComponentController1, index: number) => {
          Button('ButtonXc:' + index)
            .onClick(() => {
              console.info(`getXComponentSurfaceId = ${xc.getXComponentSurfaceId()}`);
            });
          XComponent({
            id: 'XComponent' + index,
            type: XComponentType.SURFACE,
            controller: xc
          })
            .width('100%')
            .height(200);
        });
      }.width('100%')
      .height('100%');
    }
  }

  class CustomXComponentController1 extends XComponentController {
    onSurfaceCreated(surfaceId: string): void {
      console.info(`onSurfaceCreated surfaceId: ${surfaceId}`);
    }

    onSurfaceChanged(surfaceId: string, rect: SurfaceRect): void {
      console.info(`onSurfaceChanged surfaceId: ${surfaceId}, rect: ${JSON.stringify(rect)}}`);
    }

    onSurfaceDestroyed(surfaceId: string): void {
      console.info(`onSurfaceDestroyed surfaceId: ${surfaceId}`);
    }
  }
  ```
* 方案二：不进行参数传递，在XScreen页面构造xcArray对象。

  ```ts
  @Entry
  @Component
  struct Solution2 {
    build() {
      Column() {
        XScreen2();
      }
      .height('100%')
      .width('100%');
    }
  }

  @Component
  struct XScreen2 {
    xcArray: CustomXComponentController2[] = [];

    aboutToAppear(): void {
      for (let i = 0; i < 2; i++) {
        this.xcArray.push(new CustomXComponentController2());
      }
    }

    build() {
      Column() {
        ForEach(this.xcArray, (xc: CustomXComponentController2, index: number) => {
          Button('ButtonXc:' + index)
            .onClick(() => {
              console.info(`getXComponentSurfaceId = ${xc.getXComponentSurfaceId()}`);
            });
          XComponent({
            id: 'XComponent' + index,
            type: XComponentType.SURFACE,
            controller: xc
          })
            .width('100%')
            .height(200);
        });
      }.width('100%')
      .height('100%');
    }
  }

  class CustomXComponentController2 extends XComponentController {
    onSurfaceCreated(surfaceId: string): void {
      console.info(`onSurfaceCreated surfaceId: ${surfaceId}`);
    }

    onSurfaceChanged(surfaceId: string, rect: SurfaceRect): void {
      console.info(`onSurfaceChanged surfaceId: ${surfaceId}, rect: ${JSON.stringify(rect)}}`);
    }

    onSurfaceDestroyed(surfaceId: string): void {
      console.info(`onSurfaceDestroyed surfaceId: ${surfaceId}`);
    }
  }
  ```
* 方案三：若业务场景要求需要使用状态管理进行参数传递，可以使用@Link装饰器实现。

  ```ts
  @Entry
  @Component
  struct Solution3 {
    @State xcArray: CustomXComponentController3[] = [];

    aboutToAppear(): void {
      for (let i = 0; i < 2; i++) {
        this.xcArray.push(new CustomXComponentController3());
      }
    }

    build() {
      Column() {
        XScreen3({ xcArray: this.xcArray });
      }
      .height('100%')
      .width('100%');
    }
  }

  @Component
  struct XScreen3 {
    @Link xcArray: CustomXComponentController3[];

    build() {
      Column() {
        ForEach(this.xcArray, (xc: CustomXComponentController3, index: number) => {
          Button('ButtonXc:' + index)
            .onClick(() => {
              console.info(`getXComponentSurfaceId = ${xc.getXComponentSurfaceId()}`);
            });
          XComponent({
            id: 'XComponent' + index,
            type: XComponentType.SURFACE,
            controller: xc
          })
            .width('100%')
            .height(200);
        });
      }.width('100%')
      .height('100%');
    }
  }

  class CustomXComponentController3 extends XComponentController {
    onSurfaceCreated(surfaceId: string): void {
      console.info(`onSurfaceCreated surfaceId: ${surfaceId}`);
    }

    onSurfaceChanged(surfaceId: string, rect: SurfaceRect): void {
      console.info(`onSurfaceChanged surfaceId: ${surfaceId}, rect: ${JSON.stringify(rect)}}`);
    }

    onSurfaceDestroyed(surfaceId: string): void {
      console.info(`onSurfaceDestroyed surfaceId: ${surfaceId}`);
    }
  }
  ```
