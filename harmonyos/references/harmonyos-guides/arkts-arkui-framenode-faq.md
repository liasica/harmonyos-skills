---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-arkui-framenode-faq
title: 命令式节点常见问题
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发调试调优 > UI开发常见问题 > 命令式节点常见问题
category: harmonyos-guides
scraped_at: 2026-04-29T13:29:01+08:00
doc_updated_at: 2026-04-17
content_hash: sha256:219efe93e5fe48ba2c283a95538c894c681d533676f3f1387d1b7eea7f91584a
---

本文档介绍命令式节点的常见问题并提供参考。

## FrameNode节点运行时出现jscrash

**问题现象**

不规范地使用[FrameNode](../harmonyos-references/js-apis-arkui-framenode.md)后出现[JS Crash](jscrash-guidelines.md)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/5cA8YLmyQOmrAI-eX1sduQ/zh-cn_image_0000002558764662.png?HW-CC-KV=V1&HW-CC-Date=20260429T052900Z&HW-CC-Expire=86400&HW-CC-Sign=E3BF2BD500900D351D3DD53D990E0E8D1176A39C12C38E584B970E7A3CA495AB)

**解决措施**

根据提示跳转至报错日志，查看具体的报错原因，进行相应的修改，具体的跳转方法请参考下方示例代码。

**示例代码**

该示例演示了FrameNode抛出[dispose](../harmonyos-references/js-apis-arkui-framenode.md#dispose12)相关异常的场景。运行示例代码后会出现jscrash报错，参考下方的动图，跳转至具体的报错场景，发现报错的原因是调用dispose后不能调用[getMeasuredSize](../harmonyos-references/js-apis-arkui-framenode.md#getmeasuredsize12)，在本示例中，删除dispose相关代码即可正常运行。

```
1. import { NodeController, FrameNode, typeNode } from '@kit.ArkUI';

3. // 继承NodeController实现自定义UI控制器
4. class MyNodeController extends NodeController {
5. makeNode(uiContext: UIContext): FrameNode | null {
6. let node = new FrameNode(uiContext);
7. node.dispose(); // 删除本行可以让程序正常运行
8. node.getMeasuredSize();
9. return node;
10. }
11. }

13. @Entry
14. @Component
15. struct FrameNodeTypeTest {
16. private myNodeController: MyNodeController = new MyNodeController();

18. build() {
19. Row() {
20. Text('Hello')
21. NodeContainer(this.myNodeController);
22. }
23. }
24. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/oimaFpH0SOmJsLwGBcVZ7g/zh-cn_image_0000002589324533.png?HW-CC-KV=V1&HW-CC-Date=20260429T052900Z&HW-CC-Expire=86400&HW-CC-Sign=17372845E535F1079BF47792BC8608D5B1FCADF0DF4FA3FDDFB7C085B697C697)

## Native侧创建的ArkUI\_NodeHandle执行disposeNode后出现cppcrash

**问题现象**

开发者对[ArkUI\_NodeHandle](../harmonyos-references/capi-arkui-nativemodule-arkui-node8h.md)执行[disposeNode](../harmonyos-references/capi-arkui-nativemodule-arkui-nativenodeapi-1.md#disposenode)前，未清理节点相关的资源对象（如回调、捕获引用等），导致节点下树后高概率发生程序崩溃，崩溃原因为释放后使用（Use After Free）。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fe/v3/9Xwq42FsR-KtYWbaZgphmA/zh-cn_image_0000002589244471.png?HW-CC-KV=V1&HW-CC-Date=20260429T052900Z&HW-CC-Expire=86400&HW-CC-Sign=E1C19C224F1C32D9ED7B5C9585D37B8A00F627A7A85B17347D94E9548D3E1200)

下图为此类问题的典型故障日志，日志中的Reason:Signal字段为SIGSEGV(SEGV\_MAPERR)，表示崩溃地址不固定，可能提示野指针或空指针解引用。此时崩溃栈内各个栈帧基本均为系统栈，如DetachFromMainTree、~FrameNode等系统函数，此类系统函数多与disposeNode接口和节点下树析构相关。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/B8rs1mVtRj-uKPu3OQPXdQ/zh-cn_image_0000002558764664.png?HW-CC-KV=V1&HW-CC-Date=20260429T052900Z&HW-CC-Expire=86400&HW-CC-Sign=6AA97B07FFA6BFE410CA5D9B59C24645FA02DCBDCCED79C7C76F8B4A238E52EC)

**解决措施**

调整资源释放顺序，优先释放节点衍生资源（依赖节点创建的对象与回调、捕获引用等），再释放节点。

下面提供一个cppcrash的示例。具体实现为创建[XComponent](../harmonyos-references/ts-basic-components-xcomponent.md)时调用BindNode，将TS侧XComponent传入Native侧并创建[OH\_ArkUI\_SurfaceCallback](../harmonyos-references/mponent-native-xcomponent-oh-arkui-surfacecallback.md)，在XComponent下树时调用UnbindNode回收相关资源。BindNode通过XComponent节点创建[OH\_ArkUI\_SurfaceHolder](../harmonyos-references/component-native-xcomponent-oh-arkui-surfaceholder.md)对象并注册[OH\_ArkUI\_SurfaceCallback\_SetSurfaceDestroyedEvent](../harmonyos-references/capi-native-interface-xcomponent-h.md#oh_arkui_surfacecallback_setsurfacedestroyedevent)事件。在UnbindNode中，由于XComponent的dispose在OH\_ArkUI\_SurfaceHolder调用dispose之前执行，导致后者释放时使用了已释放的XComponent节点，从而触发cppcrash。

针对上述示例，在UnbindNode函数中，把disposeNode移至函数末尾前执行，即可修复此问题。

```
1. void OnSurfaceDestroyedNative(OH_ArkUI_SurfaceHolder *holder)
2. {
3. std::string *helloWorld = reinterpret_cast<std::string *>(OH_ArkUI_SurfaceHolder_GetUserData(holder));
4. OH_LOG_Print(LOG_APP, LOG_INFO, 0xff00, "TestTag", "OnSurfaceDestroyed triggered, registered string is %{public}s",
5. helloWorld->c_str());
6. delete helloWorld;
7. }

9. napi_value UnbindNode(napi_env env, napi_callback_info info)
10. {
11. OH_LOG_Print(LOG_APP, LOG_INFO, 0xff00, "TestTag", "移除XComponent与衍生资源");
12. size_t argc = 1;
13. napi_value args[1] = {nullptr};
14. napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);
15. if (!g_node1) {
16. OH_LOG_Print(LOG_APP, LOG_ERROR, 0xff00, "TestTag", "NodeId does not exist error");
17. return nullptr;
18. }
19. nodeAPI->disposeNode(g_node1); // 在销毁SurfaceCallback与SurfaceHolder前销毁node，会引发crash
20. g_node1 = nullptr;
21. if (g_holder) {
22. OH_LOG_Print(LOG_APP, LOG_INFO, 0xff00, "TestTag", "Start Dispose SurfaceCallback");
23. OH_ArkUI_SurfaceHolder_RemoveSurfaceCallback(g_holder, g_callback); // 移除SurfaceCallback
24. OH_ArkUI_SurfaceCallback_Dispose(g_callback);                       // 销毁SurfaceCallback
25. g_callback = nullptr;
26. }
27. OH_ArkUI_SurfaceHolder_Dispose(g_holder); // 销毁SurfaceHolder
28. g_holder = nullptr;
29. // 将nodeAPI->disposeNode(g_node1);移至此处即可修复crash

31. return nullptr;
32. }

34. napi_value BindNode(napi_env env, napi_callback_info info)
35. {
36. size_t argc = 2;
37. napi_value args[2] = {nullptr};
38. napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);
39. OH_ArkUI_GetNodeHandleFromNapiValue(env, args[1], &g_node1); // 获取nodeHandle
40. g_holder = OH_ArkUI_SurfaceHolder_Create(g_node1);           // 获取SurfaceHolder
41. g_callback = OH_ArkUI_SurfaceCallback_Create();              // 创建SurfaceCallback
42. auto hello = new std::string("helloWorld");
43. OH_ArkUI_SurfaceHolder_SetUserData(g_holder, hello); // 设置std::string至SurfaceHolder
44. OH_ArkUI_SurfaceCallback_SetSurfaceDestroyedEvent(g_callback,
45. OnSurfaceDestroyedNative); // 注册OnSurfaceDestroyed回调
46. OH_ArkUI_SurfaceHolder_AddSurfaceCallback(g_holder, g_callback);             // 注册SurfaceCallback回调
47. return nullptr;
48. }
```
