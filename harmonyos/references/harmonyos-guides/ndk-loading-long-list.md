---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ndk-loading-long-list
title: 使用列表
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (基于NDK构建UI) > 构建布局 > 使用列表
category: harmonyos-guides
scraped_at: 2026-04-29T13:28:32+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:cfa6fd271aecd1c158e97019738e72292e7b5bd7a35dc037f8ce3ac05ff357d9
---

ArkUI开发框架在NDK接口提供了列表组件，使用列表可以轻松高效地显示结构化、可滚动的信息。列表组件支持控制滚动位置、支持分组显示内容、支持使用[NodeAdapter](ndk-loading-long-list.md#nodeadapter介绍)实现懒加载以提升列表创建性能。

## 创建列表

参考[接入ArkTS页面](ndk-access-the-arkts-page.md)章节实现列表创建。

## 监听滚动事件

参考[监听组件事件](ndk-listen-to-component-events.md)章节实现列表滚动事件监听。

## 使用懒加载

### NodeAdapter介绍

NDK提供了NodeAdapter对象替代ArkTS侧的[LazyForEach](../harmonyos-references/ts-rendering-control-lazyforeach.md)功能，用于按需生成子组件，NodeAdapter支持在[List](../harmonyos-references/ts-container-list.md)/[ListItemGroup](../harmonyos-references/ts-container-listitemgroup.md)、[Grid](../harmonyos-references/ts-container-grid.md)、[WaterFlow](../harmonyos-references/ts-container-waterflow.md)、[Swiper](../harmonyos-references/ts-container-swiper.md)组件中使用。

* 设置了NodeAdapter属性的节点，不支持直接通过[addChild](../harmonyos-references/capi-arkui-nativemodule-arkui-nativenodeapi-1.md#addchild)等接口添加子组件。子组件完全由NodeAdapter管理，使用属性方法设置NodeAdapter时，会判断父组件是否已经存在子节点，如果父组件已经存在子节点，则设置NodeAdapter操作失败，返回错误码。
* NodeAdapter通过相关事件通知开发者按需生成组件，类似组件事件机制，开发者使用NodeAdapter时要注册[事件监听器](../harmonyos-references/capi-native-node-h.md#oh_arkui_nodeadapter_registereventreceiver)，在监听器事件中处理逻辑，相关事件通过[ArkUI\_NodeAdapterEventType](../harmonyos-references/capi-native-node-h.md#arkui_nodeadaptereventtype)定义。另外NodeAdapter不会主动释放不在屏幕内显示的组件对象，开发者需要在[NODE\_ADAPTER\_EVENT\_ON\_REMOVE\_NODE\_FROM\_ADAPTER](../harmonyos-references/capi-native-node-h.md#arkui_nodeadaptereventtype)事件中进行组件对象的释放，或者进行缓存复用。下图展示了典型列表滑动场景下的事件触发机制：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/froNv7xgTmmHIMI__3RK_Q/zh-cn_image_0000002589324423.png?HW-CC-KV=V1&HW-CC-Date=20260429T052831Z&HW-CC-Expire=86400&HW-CC-Sign=D20073AF7C5BD84B703448E0A7597E65A6344A2F1CE34B00FA6D3358039528FD)

以下示例提供了懒加载适配器的实现方法，仅包含主要步骤，完整代码请参考[NdkCreateList](https://gitcode.com/openharmony/applications_app_samples/tree/master/code/DocsSample/ArkUISample/NativeType/NdkCreateList)。

### 实现懒加载适配器

使用ArkUIListItemAdapter类来管理懒加载适配器，在类的构造中创建NodeAdapter对象，并给NodeAdapter对象设置事件监听器，在类的析构函数中，销毁NodeAdapter对象。

ArkUIListItemAdapter类为自定义的通用模板类，模板参数类型可按业务数据和节点模型进行自定义。该模板对外开放“创建子组件”回调，用于按需创建并挂载每个ListItem对应的子组件。该模板还提供“复用ListItem”回调，用于在节点回收后执行状态重置与复用逻辑。

```
1. // ArkUIListItemAdapter.h
2. // 用于文本列表懒加载功能代码。

4. #ifndef MYAPPLICATION_ARKUILISTITEMADAPTER_H
5. #define MYAPPLICATION_ARKUILISTITEMADAPTER_H

7. #include <algorithm>
8. #include <arkui/native_node.h>
9. #include <cstddef>
10. #include <cstdint>
11. #include <functional>
12. #include <memory>
13. #include <stack>
14. #include <string>
15. #include <unordered_map>
16. #include <vector>

18. #include "ArkUIListItemNode.h"
19. #include "ArkUITextNode.h"
20. #include "NativeModule.h"

22. namespace NativeModule {

24. class IArkUIListItemAdapter {
25. public:
26. virtual ~IArkUIListItemAdapter() = default;
27. virtual ArkUI_NodeAdapterHandle GetHandle() const = 0;
28. };
29. template <typename ItemType> class ArkUIListItemAdapterT : public IArkUIListItemAdapter {
30. public:
31. // 创建列表项节点的回调类型。
32. using CreateChildCallback = std::function<std::shared_ptr<ArkUIListItemNode>(const ItemType &item, int32_t index)>;
33. // 复用列表项节点时更新内容的回调类型。
34. using ReuseListItemCallback =
35. std::function<void(const std::shared_ptr<ArkUIListItemNode> &listItem, const ItemType &item, int32_t index)>;
36. // 生成节点唯一标识的回调类型。
37. using NodeIdCallback = std::function<int64_t(const ItemType &item, int32_t index)>;

39. // 创建NodeAdapter并初始化数据及各类回调。
40. explicit ArkUIListItemAdapterT(std::vector<ItemType> data, CreateChildCallback createChildCallback,
41. ReuseListItemCallback reuseListItemCallback, NodeIdCallback nodeIdCallback = nullptr)
42. : handle_(OH_ArkUI_NodeAdapter_Create()), data_(std::move(data)),
43. createChildCallback_(std::move(createChildCallback)),
44. reuseListItemCallback_(std::move(reuseListItemCallback)), nodeIdCallback_(std::move(nodeIdCallback)) {
45. // 设置懒加载数据。
46. OH_ArkUI_NodeAdapter_SetTotalNodeCount(handle_, data_.size());
47. // 设置懒加载回调事件。
48. OH_ArkUI_NodeAdapter_RegisterEventReceiver(handle_, this, OnStaticAdapterEvent);
49. }

51. ~ArkUIListItemAdapterT() override
52. {
53. // 释放创建的组件。
54. while (!cachedItems_.empty()) {
55. cachedItems_.pop();
56. }
57. items_.clear();
58. // 释放Adapter相关资源。
59. OH_ArkUI_NodeAdapter_UnregisterEventReceiver(handle_);
60. OH_ArkUI_NodeAdapter_Dispose(handle_);
61. }

63. ArkUI_NodeAdapterHandle GetHandle() const override { return handle_; }

65. const std::vector<ItemType> &GetData() const { return data_; }

67. void SetData(std::vector<ItemType> data)
68. {
69. data_ = std::move(data);
70. OH_ArkUI_NodeAdapter_SetTotalNodeCount(handle_, data_.size());
71. OH_ArkUI_NodeAdapter_ReloadAllItems(handle_);
72. }

74. void SetNodeIdCallback(NodeIdCallback callback) { nodeIdCallback_ = std::move(callback); }

76. void RemoveItem(size_t index)
77. {
78. // 删除第index个数据。
79. if (index >= data_.size()) {
80. return;
81. }
82. data_.erase(data_.begin() + static_cast<std::ptrdiff_t>(index));
83. // 如果index会导致可视区域元素发生可见性变化，则会回调NODE_ADAPTER_EVENT_ON_REMOVE_NODE_FROM_ADAPTER事件删除元素，
84. // 根据是否有新增元素回调NODE_ADAPTER_EVENT_ON_GET_NODE_ID和NODE_ADAPTER_EVENT_ON_ADD_NODE_TO_ADAPTER事件。
85. OH_ArkUI_NodeAdapter_RemoveItem(handle_, index, 1);
86. // 更新新的数量。
87. OH_ArkUI_NodeAdapter_SetTotalNodeCount(handle_, data_.size());
88. }

90. void InsertItem(int32_t index, const ItemType &value)
91. {
92. int32_t safeIndex = std::max(0, std::min(index, static_cast<int32_t>(data_.size())));
93. data_.insert(data_.begin() + safeIndex, value);
94. // 如果index会导致可视区域元素发生可见性变化，则会回调NODE_ADAPTER_EVENT_ON_GET_NODE_ID和NODE_ADAPTER_EVENT_ON_ADD_NODE_TO_ADAPTER事件，
95. // 根据是否有删除元素回调NODE_ADAPTER_EVENT_ON_REMOVE_NODE_FROM_ADAPTER事件。
96. OH_ArkUI_NodeAdapter_InsertItem(handle_, safeIndex, 1);
97. // 更新新的数量。
98. OH_ArkUI_NodeAdapter_SetTotalNodeCount(handle_, data_.size());
99. }

101. void MoveItem(int32_t oldIndex, int32_t newIndex)
102. {
103. if (!IsValidIndex(oldIndex) || !IsValidIndex(newIndex) || oldIndex == newIndex) {
104. return;
105. }
106. auto temp = data_[oldIndex];
107. data_.insert(data_.begin() + newIndex, temp);
108. int32_t removeIndex = oldIndex;
109. if (newIndex < oldIndex) {
110. removeIndex += 1;
111. }
112. data_.erase(data_.begin() + removeIndex);
113. // 移到位置如果未发生可视区域内元素的可见性变化，则不回调事件，反之根据新增和删除场景回调对应的事件。
114. OH_ArkUI_NodeAdapter_MoveItem(handle_, oldIndex, newIndex);
115. }

117. void ReloadItem(int32_t index, const ItemType &value)
118. {
119. if (!IsValidIndex(index)) {
120. return;
121. }
122. data_[index] = value;
123. // 如果index位于可视区域内，先回调NODE_ADAPTER_EVENT_ON_REMOVE_NODE_FROM_ADAPTER删除老元素，
124. // 再回调NODE_ADAPTER_EVENT_ON_GET_NODE_ID和NODE_ADAPTER_EVENT_ON_ADD_NODE_TO_ADAPTER事件。
125. OH_ArkUI_NodeAdapter_ReloadItem(handle_, index, 1);
126. }

128. void ReloadAllItem()
129. {
130. // 全部重新加载场景下，会回调NODE_ADAPTER_EVENT_ON_GET_NODE_ID接口获取新的组件ID，
131. // 根据新的组件ID进行对比，ID不发生变化的进行复用，
132. // 针对新增ID的元素，调用NODE_ADAPTER_EVENT_ON_ADD_NODE_TO_ADAPTER事件创建新的组件，
133. // 然后判断老数据中遗留的未使用ID，调用NODE_ADAPTER_EVENT_ON_REMOVE_NODE_FROM_ADAPTER删除老元素。
134. OH_ArkUI_NodeAdapter_ReloadAllItems(handle_);
135. }

137. private:
138. struct ItemEntry {
139. std::shared_ptr<ArkUIListItemNode> listItem = nullptr;
140. };

142. static void OnStaticAdapterEvent(ArkUI_NodeAdapterEvent *event)
143. {
144. // 获取实例对象，回调实例事件。
145. auto *itemAdapter = reinterpret_cast<ArkUIListItemAdapterT *>(OH_ArkUI_NodeAdapterEvent_GetUserData(event));
146. if (itemAdapter != nullptr) {
147. itemAdapter->OnAdapterEvent(event);
148. }
149. }

151. void OnAdapterEvent(ArkUI_NodeAdapterEvent *event)
152. {
153. // 获取事件类型
154. auto type = OH_ArkUI_NodeAdapterEvent_GetType(event);
155. switch (type) {
156. // Adapter需要添加新元素时获取新元素的唯一标识符
157. case NODE_ADAPTER_EVENT_ON_GET_NODE_ID:
158. OnNewItemIdCreated(event);
159. break;
160. // Adapter需要添加新元素时获取新元素的内容
161. case NODE_ADAPTER_EVENT_ON_ADD_NODE_TO_ADAPTER:
162. OnNewItemAttached(event);
163. break;
164. // Adapter将元素移除
165. case NODE_ADAPTER_EVENT_ON_REMOVE_NODE_FROM_ADAPTER:
166. OnItemDetached(event);
167. break;
168. default:
169. break;
170. }
171. }

173. // 分配ID给需要显示的Item，用于ReloadAllItems场景的元素diff。
174. void OnNewItemIdCreated(ArkUI_NodeAdapterEvent *event)
175. {
176. auto index = OH_ArkUI_NodeAdapterEvent_GetItemIndex(event);
177. if (!IsValidIndex(index)) {
178. return;
179. }
180. int64_t id = nodeIdCallback_ ? nodeIdCallback_(data_[index], index) : static_cast<int64_t>(index);
181. OH_ArkUI_NodeAdapterEvent_SetNodeId(event, id);
182. }

184. // 需要新的Item显示在可见区域。
185. void OnNewItemAttached(ArkUI_NodeAdapterEvent *event)
186. {
187. auto index = OH_ArkUI_NodeAdapterEvent_GetItemIndex(event);
188. if (!IsValidIndex(index)) {
189. return;
190. }

192. ItemEntry itemEntry;
193. if (!cachedItems_.empty()) {
194. // 使用并更新回收复用的缓存。
195. itemEntry = cachedItems_.top();
196. // 释放缓存池的引用。
197. cachedItems_.pop();
198. reuseListItemCallback_(itemEntry.listItem, data_[index], index);
199. } else {
200. // 创建新的元素。
201. itemEntry.listItem = createChildCallback_(data_[index], index);
202. }
203. if (itemEntry.listItem == nullptr) {
204. itemEntry.listItem = std::make_shared<ArkUIListItemNode>();
205. }

207. auto handle = itemEntry.listItem->GetHandle();
208. items_[handle] = itemEntry;
209. // 设置需要展示的元素。
210. OH_ArkUI_NodeAdapterEvent_SetItem(event, handle);
211. }
212. // Item从可见区域移除。
213. void OnItemDetached(ArkUI_NodeAdapterEvent *event)
214. {
215. auto item = OH_ArkUI_NodeAdapterEvent_GetRemovedNode(event);
216. auto iter = items_.find(item);
217. if (iter != items_.end()) {
218. // 放置到缓存池中进行回收复用。
219. cachedItems_.push(iter->second);
220. items_.erase(iter);
221. }
222. }

224. bool IsValidIndex(int32_t index) const { return index >= 0 && index < static_cast<int32_t>(data_.size()); }

226. // NodeAdapter实例句柄。
227. ArkUI_NodeAdapterHandle handle_ = nullptr;
228. // 列表数据源。
229. std::vector<ItemType> data_;
230. // 创建列表项节点回调。
231. CreateChildCallback createChildCallback_ = nullptr;
232. // 复用列表项节点回调。
233. ReuseListItemCallback reuseListItemCallback_ = nullptr;
234. // 节点ID生成回调。
235. NodeIdCallback nodeIdCallback_ = nullptr;
236. // 管理NodeAdapter生成的元素。
237. std::unordered_map<ArkUI_NodeHandle, ItemEntry> items_;

239. // 管理回收复用组件池。
240. std::stack<ItemEntry> cachedItems_;
241. };
242. } // namespace NativeModule

244. #endif // MYAPPLICATION_ARKUILISTITEMADAPTER_H
```

[ArkUIListItemAdapter.h](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/NativeType/NdkCreateList/entry/src/main/cpp/ArkUIListItemAdapter.h#L15-L243)

### 在列表中应用懒加载适配器

1. 在ArkUIListNode中添加SetLazyAdapter函数，给列表节点设置[NODE\_LIST\_NODE\_ADAPTER](../harmonyos-references/capi-native-node-h.md#arkui_nodeattributetype)属性，并将NodeAdapter作为属性入参传入。

   ```
   1. // ArkUIListNode.h
   2. // 提供列表组件的封装。
   3. #ifndef MYAPPLICATION_ARKUILISTNODE_H
   4. #define MYAPPLICATION_ARKUILISTNODE_H

   6. #include "ArkUINode.h"
   7. #include "ArkUIListItemAdapter.h"
   8. namespace NativeModule {
   9. class ArkUIListNode : public ArkUINode {
   10. public:
   11. ArkUIListNode() // 创建ArkUI的列表组件。
   12. : ArkUINode((NativeModuleInstance::GetInstance()->GetNativeNodeAPI())->createNode(ARKUI_NODE_LIST)) {}

   14. ~ArkUIListNode() override
   15. {
   16. if (nativeModule_) {
   17. nativeModule_->unregisterNodeEvent(handle_, NODE_LIST_ON_SCROLL_INDEX);
   18. if (adapter_) {
   19. // 析构的时候卸载adapter下的UI组件。
   20. nativeModule_->resetAttribute(handle_, NODE_LIST_NODE_ADAPTER);
   21. adapter_.reset();
   22. }
   23. }
   24. }
   25. // List组件的属性接口封装。
   26. void SetScrollBarState(bool isShow)
   27. {
   28. ArkUI_ScrollBarDisplayMode displayMode =
   29. isShow ? ARKUI_SCROLL_BAR_DISPLAY_MODE_ON : ARKUI_SCROLL_BAR_DISPLAY_MODE_OFF;
   30. ArkUI_NumberValue value[] = {{.i32 = displayMode}};
   31. ArkUI_AttributeItem item = {value, 1};
   32. nativeModule_->setAttribute(handle_, NODE_SCROLL_BAR_DISPLAY_MODE, &item);
   33. }

   35. void RegisterOnScrollIndex(const std::function<void(int32_t index)> &onScrollIndex)
   36. {
   37. onScrollIndex_ = onScrollIndex;
   38. nativeModule_->registerNodeEvent(handle_, NODE_LIST_ON_SCROLL_INDEX, 0, nullptr);
   39. }
   40. // 引入懒加载模块。
   41. void SetLazyAdapter(const std::shared_ptr<IArkUIListItemAdapter> &adapter)
   42. {
   43. if (!adapter) {
   44. nativeModule_->resetAttribute(handle_, NODE_LIST_NODE_ADAPTER);
   45. adapter_.reset();
   46. return;
   47. }
   48. ArkUI_AttributeItem item{nullptr, 0, nullptr, adapter->GetHandle()};
   49. nativeModule_->setAttribute(handle_, NODE_LIST_NODE_ADAPTER, &item);
   50. adapter_ = adapter;
   51. }
   52. // ...
   53. protected:
   54. void OnNodeEvent(ArkUI_NodeEvent *event) override
   55. {
   56. auto eventType = OH_ArkUI_NodeEvent_GetEventType(event);
   57. switch (eventType) {
   58. case NODE_LIST_ON_SCROLL_INDEX: {
   59. auto index = OH_ArkUI_NodeEvent_GetNodeComponentEvent(event)->data[0];
   60. if (onScrollIndex_) {
   61. onScrollIndex_(index.i32);
   62. }
   63. break;
   64. }
   65. default: {
   66. break;
   67. }
   68. }
   69. }

   71. private:
   72. std::function<void(int32_t index)> onScrollIndex_;

   74. std::shared_ptr<IArkUIListItemAdapter> adapter_;
   75. };
   76. } // namespace NativeModule

   78. #endif // MYAPPLICATION_ARKUILISTNODE_H
   ```

   [ArkUIListNode.h](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/NativeType/NdkCreateList/entry/src/main/cpp/ArkUIListNode.h#L15-L146)
2. 创建List使用懒加载的示例代码，调用List节点的SetLazyAdapter接口设置懒加载适配器。

   ```
   1. // LazyTextListExample
   2. // 懒加载列表示例代码。

   4. #ifndef MYAPPLICATION_LAZYTEXTLISTEXAMPLE1_H
   5. #define MYAPPLICATION_LAZYTEXTLISTEXAMPLE1_H

   7. #include "ArkUIBaseNode.h"
   8. #include "ArkUIListNode.h"
   9. #include "ArkUITextNode.h"

   11. #include <algorithm>
   12. #include <memory>
   13. #include <string>
   14. #include <vector>

   16. namespace NativeModule {
   17. // ...
   18. std::shared_ptr<ArkUIBaseNode> CreateLazyTextListExample1()
   19. {
   20. // 创建组件并挂载。
   21. // 1：创建List组件。
   22. auto list = std::make_shared<ArkUIListNode>();
   23. list->SetPercentWidth(1); // 1：宽度
   24. list->SetPercentHeight(1); // 1：高度
   25. auto data = BuildSampleData();

   27. auto adapterWeakHolder = std::make_shared<std::weak_ptr<StringAdapter>>();
   28. // 2：创建ListItem及其子组件的回调。
   29. auto createChildCallback = [adapterWeakHolder](const std::string &item,
   30. int32_t index) -> std::shared_ptr<ArkUIListItemNode> {
   31. (void)index;
   32. return BuildListItemNode(item, adapterWeakHolder);
   33. };
   34. // 3：复用ListItem的回调。
   35. auto reuseListItemCallback = [adapterWeakHolder](const std::shared_ptr<ArkUIListItemNode> &listItem,
   36. const std::string &item, int32_t index) {
   37. (void)index;
   38. ReuseListItemNode(listItem, item, adapterWeakHolder);
   39. };

   41. auto adapter = std::make_shared<StringAdapter>(data, createChildCallback, reuseListItemCallback);
   42. *adapterWeakHolder = adapter;
   43. // 4：创建ListItem懒加载组件并挂载到List中。
   44. list->SetLazyAdapter(adapter);
   45. return list;
   46. }

   48. } // namespace NativeModule

   50. #endif // MYAPPLICATION_LAZYTEXTLISTEXAMPLE1_H
   ```

   [LazyTextListExample1.h](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/NativeType/NdkCreateList/entry/src/main/cpp/LazyTextListExample1.h#L15-L42)
3. 在NativeEntry.cpp中调用List使用懒加载的示例代码。

   ```
   1. // NDK接口入口挂载文件。

   3. #include "NativeEntry.h"

   5. #include "LazyTextListExample.h"
   6. #include "LazyTextListExample1.h"

   8. #include <arkui/native_node_napi.h>
   9. #include <arkui/native_type.h>
   10. #include <js_native_api.h>
   11. #include <algorithm>
   12. #include <memory>
   13. #include <string>
   14. #include <uv.h>
   15. #include <vector>

   17. namespace NativeModule {

   19. // ...

   21. napi_value CreateNativeRoot(napi_env env, napi_callback_info info)
   22. {
   23. size_t argc = 1;
   24. napi_value args[1] = {nullptr};

   26. napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);

   28. // 获取NodeContent。
   29. ArkUI_NodeContentHandle contentHandle;
   30. OH_ArkUI_GetNodeContentFromNapiValue(env, args[0], &contentHandle);
   31. NativeEntry::GetInstance()->SetContentHandle(contentHandle);

   33. // 创建懒加载文本列表。
   34. auto node = CreateLazyTextListExample();

   36. // 保存Native侧对象到管理类中，维护生命周期。
   37. NativeEntry::GetInstance()->SetRootNode(node);
   38. return nullptr;
   39. }

   41. napi_value DestroyNativeRoot(napi_env env, napi_callback_info info)
   42. {
   43. // 从管理类中释放Native侧对象。
   44. NativeEntry::GetInstance()->DisposeRootNode();
   45. return nullptr;
   46. }

   48. } // namespace NativeModule
   ```

   [NativeEntry.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/NativeType/NdkCreateList/entry/src/main/cpp/NativeEntry.cpp#L15-L92)

## 控制列表滚动位置

1. 控制列表滚动到指定偏移量位置。

   ```
   1. // ArkUIListNode.h
   2. // 提供列表组件的封装。
   3. // ...
   4. class ArkUIListNode : public ArkUINode {
   5. public:
   6. // ...
   7. void ScrollTo(float offset)
   8. {
   9. ArkUI_NumberValue value[] = {{.f32 = 0}, {.f32 = offset}, {.f32 = 0}};
   10. ArkUI_AttributeItem Item = {.value = value, .size = 3};
   11. nativeModule_->setAttribute(handle_, NODE_SCROLL_OFFSET, &Item);
   12. }
   13. // ...
   14. };
   ```

   [ArkUIListNode.h](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/NativeType/NdkCreateList/entry/src/main/cpp/ArkUIListNode.h#L16-L139)
2. 控制列表滚动到指定元素。

   ```
   1. // ArkUIListNode.h
   2. // 提供列表组件的封装。
   3. // ...
   4. class ArkUIListNode : public ArkUINode {
   5. public:
   6. // ...
   7. void ScrollToIndex(int32_t index)
   8. {
   9. ArkUI_NumberValue value[] = {{.i32 = index}};
   10. ArkUI_AttributeItem Item = {.value = value, .size = 1};
   11. nativeModule_->setAttribute(handle_, NODE_LIST_SCROLL_TO_INDEX, &Item);
   12. }
   13. // ...
   14. };
   ```

   [ArkUIListNode.h](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/NativeType/NdkCreateList/entry/src/main/cpp/ArkUIListNode.h#L17-L141)
3. 控制列表滚动指定偏移量。

   ```
   1. // ArkUIListNode.h
   2. // 提供列表组件的封装。
   3. // ...
   4. class ArkUIListNode : public ArkUINode {
   5. public:
   6. // ...
   7. void ScrollBy(float offset)
   8. {
   9. ArkUI_NumberValue value[] = {{.f32 = 0}, {.f32 = offset}};
   10. ArkUI_AttributeItem Item = {.value = value, .size = 2};
   11. nativeModule_->setAttribute(handle_, NODE_SCROLL_BY, &Item);
   12. }
   13. // ...
   14. };
   ```

   [ArkUIListNode.h](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/NativeType/NdkCreateList/entry/src/main/cpp/ArkUIListNode.h#L19-L142)

## ListItem横划删除

1. [ListItem](../harmonyos-references/ts-container-listitem.md)设置[NODE\_LIST\_ITEM\_SWIPE\_ACTION](../harmonyos-references/capi-native-node-h.md#arkui_nodeattributetype)属性，将[ArkUI\_ListItemSwipeActionOption](../harmonyos-references/arkui-nativemodule-arkui-listitemswipeactionoption.md)对象作为属性参数传入。

   ```
   1. // ArkUIListItemNode.h
   2. // 提供列表项的封装类。
   3. #ifndef MYAPPLICATION_ARKUILISTITEMNODE_H
   4. #define MYAPPLICATION_ARKUILISTITEMNODE_H
   5. #include "ArkUINode.h"
   6. namespace NativeModule {
   7. class ArkUIListItemNode : public ArkUINode {
   8. public:
   9. ArkUIListItemNode()
   10. : ArkUINode((NativeModuleInstance::GetInstance()->GetNativeNodeAPI())->createNode(ARKUI_NODE_LIST_ITEM)) {}
   11. ~ArkUIListItemNode() override
   12. {
   13. // 销毁ListItemSwipeActionOption实例
   14. if (swipeAction_) {
   15. OH_ArkUI_ListItemSwipeActionOption_Dispose(swipeAction_);
   16. }
   17. // 销毁ListItemSwipeActionItem实例
   18. if (swipeItem_) {
   19. OH_ArkUI_ListItemSwipeActionItem_Dispose(swipeItem_);
   20. }
   21. }
   22. void SetSwiperAction(std::shared_ptr<ArkUINode> node)
   23. {
   24. swipeContent_ = node;
   25. // 创建ListItemSwipeActionItem接口设置的配置项
   26. swipeItem_ = OH_ArkUI_ListItemSwipeActionItem_Create();
   27. // 设置ListItemSwipeActionItem的布局内容
   28. OH_ArkUI_ListItemSwipeActionItem_SetContent(swipeItem_, node->GetHandle());
   29. // 创建ListItemSwipeActionOption接口设置的配置项
   30. swipeAction_ = OH_ArkUI_ListItemSwipeActionOption_Create();
   31. // 设置ListItemSwipeActionItem的右侧（垂直布局）或下方（横向布局）布局内容
   32. OH_ArkUI_ListItemSwipeActionOption_SetEnd(swipeAction_, swipeItem_);
   33. ArkUI_AttributeItem Item = {.object = swipeAction_};
   34. nativeModule_->setAttribute(handle_, NODE_LIST_ITEM_SWIPE_ACTION, &Item);
   35. }
   36. std::shared_ptr<ArkUINode> GetSwipeContent() const { return swipeContent_; }

   38. private:
   39. ArkUI_ListItemSwipeActionOption *swipeAction_ = nullptr;
   40. ArkUI_ListItemSwipeActionItem *swipeItem_ = nullptr;
   41. std::shared_ptr<ArkUINode> swipeContent_ = nullptr;
   42. };
   43. } // namespace NativeModule
   44. #endif // MYAPPLICATION_ARKUILISTITEMNODE_H
   ```

   [ArkUIListItemNode.h](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/NativeType/NdkCreateList/entry/src/main/cpp/ArkUIListItemNode.h#L15-L54)
2. 设置创建ListItem和复用ListItem的回调函数。当创建[ListItem](../harmonyos-references/ts-container-listitem.md)时，创建ListItem的划出组件，并绑定点击事件，在点击事件中执行删除数据源操作。ListItem复用时，更新划出组件的绑定事件。

   ```
   1. // LazyTextListExample
   2. // 懒加载列表示例代码。

   4. #ifndef MYAPPLICATION_LAZYTEXTLISTEXAMPLE1_H
   5. #define MYAPPLICATION_LAZYTEXTLISTEXAMPLE1_H

   7. #include "ArkUIBaseNode.h"
   8. #include "ArkUIListNode.h"
   9. #include "ArkUITextNode.h"

   11. #include <algorithm>
   12. #include <memory>
   13. #include <string>
   14. #include <vector>

   16. namespace NativeModule {
   17. using StringAdapter = ArkUIListItemAdapterT<std::string>;
   18. using AdapterWeakHolder = std::shared_ptr<std::weak_ptr<StringAdapter>>;

   20. std::vector<std::string> BuildSampleData()
   21. {
   22. std::vector<std::string> data;
   23. data.reserve(1000); // 每个分组预分配1000条数据空间。
   24. for (int32_t i = 0; i < 1000; i++) { // 1000：1000条数据空间
   25. data.emplace_back(std::to_string(i));
   26. }
   27. return data;
   28. }

   30. void RegisterDeleteClick(const std::shared_ptr<ArkUINode> &target, const AdapterWeakHolder &adapterWeakHolder,
   31. const std::string &item)
   32. {
   33. // 为删除区域注册点击事件：通过弱引用获取适配器，避免回调长期持有强引用。
   34. target->RegisterOnClick([adapterWeakHolder, item](ArkUI_NodeEvent *event) {
   35. (void)event;
   36. auto adapter = adapterWeakHolder->lock();
   37. if (!adapter) {
   38. return;
   39. }
   40. // 基于当前数据查找当前 item，确保复用场景下删除的是最新绑定项。
   41. const auto &currentData = adapter->GetData();
   42. auto it = std::find(currentData.begin(), currentData.end(), item);
   43. if (it != currentData.end()) {
   44. // RemoveItem 需要索引，这里把迭代器位置转换为 size_t。
   45. auto removeIndex = static_cast<size_t>(std::distance(currentData.begin(), it));
   46. adapter->RemoveItem(removeIndex);
   47. }
   48. });
   49. }

   51. std::shared_ptr<ArkUIListItemNode> BuildListItemNode(const std::string &item,
   52. const AdapterWeakHolder &adapterWeakHolder)
   53. {
   54. // 构建一个 ListItem：主文本区域 + 右滑删除操作区。
   55. auto listItem = std::make_shared<ArkUIListItemNode>();

   57. // 主内容文本，展示当前数据项。
   58. auto textNode = std::make_shared<ArkUITextNode>();
   59. textNode->SetTextContent(item);
   60. // ...
   61. listItem->AddChild(textNode);

   63. // 右滑动作区文本，点击后触发删除当前 item。
   64. auto swipeNode = std::make_shared<ArkUITextNode>();
   65. swipeNode->SetTextContent("del");
   66. // ...
   67. RegisterDeleteClick(swipeNode, adapterWeakHolder, item);
   68. listItem->SetSwiperAction(swipeNode);
   69. return listItem;
   70. }

   72. void ReuseListItemNode(const std::shared_ptr<ArkUIListItemNode> &listItem, const std::string &item,
   73. const AdapterWeakHolder &adapterWeakHolder)
   74. {
   75. auto &children = listItem->GetChildren();
   76. if (children.empty()) {
   77. return;
   78. }
   79. auto textNode = std::dynamic_pointer_cast<ArkUITextNode>(children.front());
   80. if (textNode) {
   81. textNode->SetTextContent(item);
   82. textNode->SetBackgroundColor(0xFFfffacd);
   83. }
   84. auto swipeContent = listItem->GetSwipeContent();
   85. if (swipeContent) {
   86. RegisterDeleteClick(swipeContent, adapterWeakHolder, item);
   87. }
   88. }

   90. // ...

   92. } // namespace NativeModule

   94. #endif // MYAPPLICATION_LAZYTEXTLISTEXAMPLE1_H
   ```
3. 添加新的ListItem时，优先复用已缓存的[ListItem](../harmonyos-references/ts-container-listitem.md)实例，并更新其内容；若无可用缓存，则创建新的ListItem。当回调返回空时，创建一个默认的ListItem作为兜底方案。最后，将生成的节点句柄回填至[OH\_ArkUI\_NodeAdapterEvent\_SetItem](../harmonyos-references/capi-native-node-h.md#oh_arkui_nodeadapterevent_setitem)事件中，完成绑定。

   ```
   1. // ArkUIListItemAdapter.h
   2. // ...
   3. template <typename ItemType> class ArkUIListItemAdapterT : public IArkUIListItemAdapter {
   4. // ...
   5. // 需要新的Item显示在可见区域。
   6. void OnNewItemAttached(ArkUI_NodeAdapterEvent *event)
   7. {
   8. auto index = OH_ArkUI_NodeAdapterEvent_GetItemIndex(event);
   9. if (!IsValidIndex(index)) {
   10. return;
   11. }

   13. ItemEntry itemEntry;
   14. if (!cachedItems_.empty()) {
   15. // 使用并更新回收复用的缓存。
   16. itemEntry = cachedItems_.top();
   17. // 释放缓存池的引用。
   18. cachedItems_.pop();
   19. reuseListItemCallback_(itemEntry.listItem, data_[index], index);
   20. } else {
   21. // 创建新的元素。
   22. itemEntry.listItem = createChildCallback_(data_[index], index);
   23. }
   24. if (itemEntry.listItem == nullptr) {
   25. itemEntry.listItem = std::make_shared<ArkUIListItemNode>();
   26. }

   28. auto handle = itemEntry.listItem->GetHandle();
   29. items_[handle] = itemEntry;
   30. // 设置需要展示的元素。
   31. OH_ArkUI_NodeAdapterEvent_SetItem(event, handle);
   32. }
   33. // ...
   34. };
   ```

   [ArkUIListItemAdapter.h](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/NativeType/NdkCreateList/entry/src/main/cpp/ArkUIListItemAdapter.h#L16-L238)
4. ArkUIListItemAdapter中新增RemoveItem，用于删除数据源并且调用[OH\_ArkUI\_NodeAdapter\_RemoveItem](../harmonyos-references/capi-native-node-h.md#oh_arkui_nodeadapter_removeitem)接口通知框架刷新UI。

   ```
   1. // ArkUIListItemAdapter.h
   2. // ...
   3. template <typename ItemType> class ArkUIListItemAdapterT : public IArkUIListItemAdapter {
   4. // ...
   5. void RemoveItem(size_t index)
   6. {
   7. // 删除第index个数据。
   8. if (index >= data_.size()) {
   9. return;
   10. }
   11. data_.erase(data_.begin() + static_cast<std::ptrdiff_t>(index));
   12. // 如果index会导致可视区域元素发生可见性变化，则会回调NODE_ADAPTER_EVENT_ON_REMOVE_NODE_FROM_ADAPTER事件删除元素，
   13. // 根据是否有新增元素回调NODE_ADAPTER_EVENT_ON_GET_NODE_ID和NODE_ADAPTER_EVENT_ON_ADD_NODE_TO_ADAPTER事件。
   14. OH_ArkUI_NodeAdapter_RemoveItem(handle_, index, 1);
   15. // 更新新的数量。
   16. OH_ArkUI_NodeAdapter_SetTotalNodeCount(handle_, data_.size());
   17. }

   19. // ...
   20. };
   ```

   [ArkUIListItemAdapter.h](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/NativeType/NdkCreateList/entry/src/main/cpp/ArkUIListItemAdapter.h#L17-L239)

## 使用分组列表

1. 分组列表使用[ListItemGroup](../harmonyos-references/ts-container-listitemgroup.md)组件实现，ListItemGroup支持添加[header](../harmonyos-references/ts-container-listitemgroup.md#listitemgroupoptions对象说明)、[footer](../harmonyos-references/ts-container-listitemgroup.md#listitemgroupoptions对象说明)设置函数，支持使用懒加载。

   ```
   1. // ArkUIListItemGroupNode.h

   3. #ifndef MYAPPLICATION_ARKUILISTITEMGROUPNODE_H
   4. #define MYAPPLICATION_ARKUILISTITEMGROUPNODE_H

   6. #include "ArkUINode.h"
   7. #include "ArkUIListItemAdapter.h"

   9. namespace NativeModule {

   11. class ArkUIListItemGroupNode : public ArkUINode {
   12. public:
   13. ArkUIListItemGroupNode()
   14. : ArkUINode((NativeModuleInstance::GetInstance()->GetNativeNodeAPI())->createNode(ARKUI_NODE_LIST_ITEM_GROUP))
   15. {
   16. }

   18. void SetHeader(const std::shared_ptr<ArkUINode> &node)
   19. {
   20. if (node) {
   21. // 创建一个属性项，把节点的句柄放进去，并设置头部
   22. ArkUI_AttributeItem item = {.object = node->GetHandle()};
   23. nativeModule_->setAttribute(handle_, NODE_LIST_ITEM_GROUP_SET_HEADER, &item);
   24. header_ = node;
   25. } else {
   26. // 如果传入的是空指针（nullptr），说明要移除已有的头部
   27. nativeModule_->resetAttribute(handle_, NODE_LIST_ITEM_GROUP_SET_HEADER);
   28. header_.reset();
   29. }
   30. }

   32. void SetFooter(const std::shared_ptr<ArkUINode> &node)
   33. {
   34. if (node) {
   35. // 创建一个属性项，把节点的句柄放进去，并设置尾部
   36. ArkUI_AttributeItem item = {.object = node->GetHandle()};
   37. nativeModule_->setAttribute(handle_, NODE_LIST_ITEM_GROUP_SET_FOOTER, &item);
   38. footer_ = node;
   39. } else {
   40. // 如果传入的是空指针（nullptr），说明要移除已有的尾部
   41. nativeModule_->resetAttribute(handle_, NODE_LIST_ITEM_GROUP_SET_FOOTER);
   42. footer_.reset();
   43. }
   44. }

   46. std::shared_ptr<ArkUINode> GetHeader() const
   47. {
   48. return header_;
   49. }

   51. std::shared_ptr<ArkUINode> GetFooter() const
   52. {
   53. return footer_;
   54. }

   56. // 引入懒加载模块。
   57. void SetLazyAdapter(const std::shared_ptr<IArkUIListItemAdapter> &adapter)
   58. {
   59. if (!adapter) {
   60. nativeModule_->resetAttribute(handle_, NODE_LIST_ITEM_GROUP_NODE_ADAPTER);
   61. adapter_.reset();
   62. return;
   63. }
   64. ArkUI_AttributeItem item{nullptr, 0, nullptr, adapter->GetHandle()};
   65. nativeModule_->setAttribute(handle_, NODE_LIST_ITEM_GROUP_NODE_ADAPTER, &item);
   66. adapter_ = adapter;
   67. }
   68. private:
   69. std::shared_ptr<ArkUINode> header_;
   70. std::shared_ptr<ArkUINode> footer_;
   71. std::shared_ptr<IArkUIListItemAdapter> adapter_;
   72. };
   73. }
   74. #endif // MYAPPLICATION_ARKUILISTITEMGROUPNODE_H
   ```

   [ArkUIListItemGroupNode.h](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/NativeType/NdkCreateList/entry/src/main/cpp/ArkUIListItemGroupNode.h#L16-L69)
2. [List](../harmonyos-references/ts-container-list.md)组件设置吸顶。

   ```
   1. // ArkUIListNode.h
   2. // 提供列表组件的封装。
   3. // ...
   4. class ArkUIListNode : public ArkUINode {
   5. // ...
   6. void SetSticky(ArkUI_StickyStyle style)
   7. {
   8. ArkUI_NumberValue value[] = {{.i32 = style}};
   9. ArkUI_AttributeItem item = {value, 1};
   10. nativeModule_->setAttribute(handle_, NODE_LIST_STICKY, &item);
   11. }
   12. // ...
   13. };
   ```

   [ArkUIListNode.h](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/NativeType/NdkCreateList/entry/src/main/cpp/ArkUIListNode.h#L18-L140)
3. [List](../harmonyos-references/ts-container-list.md)组件下使用[ListItemGroup](../harmonyos-references/ts-container-listitemgroup.md)实现分组列表界面。

   ```
   1. // LazyTextListExample.h
   2. // 懒加载列表示例代码。

   4. #ifndef MYAPPLICATION_LAZYTEXTLISTEXAMPLE_H
   5. #define MYAPPLICATION_LAZYTEXTLISTEXAMPLE_H

   7. #include "ArkUIBaseNode.h"
   8. #include "ArkUIListItemAdapter.h"
   9. #include "ArkUIListItemGroupNode.h"
   10. #include "ArkUIListNode.h"
   11. #include "ArkUITextNode.h"

   13. #include <string>
   14. #include <vector>

   16. namespace NativeModule {
   17. // ...
   18. std::shared_ptr<ArkUIListItemGroupNode> CreateListItemGroup()
   19. {
   20. auto header = std::make_shared<ArkUITextNode>();
   21. header->SetTextContent("header");
   22. header->SetFontSize(16); // 16：字体大小
   23. header->SetPercentWidth(1); // 1：宽度
   24. header->SetHeight(50); // 50：高度
   25. header->SetBackgroundColor(0xFFDCDCDC);
   26. header->SetTextAlign(ARKUI_TEXT_ALIGNMENT_CENTER);

   28. auto listItemGroup = std::make_shared<ArkUIListItemGroupNode>();
   29. listItemGroup->SetHeader(header);

   31. auto groupData = BuildGroupData();
   32. auto createChildCallback = [](const std::string &item, int32_t index) -> std::shared_ptr<ArkUIListItemNode> {
   33. return BuildListItemNode(item, index);
   34. };
   35. auto reuseListItemCallback = [](const std::shared_ptr<ArkUIListItemNode> &listItem, const std::string &item,
   36. int32_t index) {
   37. ReuseListItemNode(listItem, item, index);
   38. };

   40. auto adapter = std::make_shared<ArkUIListItemAdapterT<std::string>>(groupData, createChildCallback,
   41. reuseListItemCallback);
   42. listItemGroup->SetLazyAdapter(adapter);
   43. return listItemGroup;
   44. }

   46. std::shared_ptr<ArkUIBaseNode> CreateLazyTextListExample()
   47. {
   48. // 创建组件并挂载。
   49. // 1：创建List组件。
   50. auto list = std::make_shared<ArkUIListNode>();
   51. list->SetPercentWidth(1); // 1：宽度
   52. list->SetPercentHeight(1); // 1：高度
   53. list->SetSticky(ARKUI_STICKY_STYLE_BOTH);

   55. // 2：创建ListItemGroup并挂载到List上。
   56. for (int32_t i = 0; i < 3; i++) { // 3：分组数
   57. list->AddChild(CreateListItemGroup());
   58. }
   59. return list;
   60. }

   62. } // namespace NativeModule

   64. #endif // MYAPPLICATION_LAZYTEXTLISTEXAMPLE_H
   ```

   [LazyTextListExample.h](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/NativeType/NdkCreateList/entry/src/main/cpp/LazyTextListExample.h#L15-L55)
