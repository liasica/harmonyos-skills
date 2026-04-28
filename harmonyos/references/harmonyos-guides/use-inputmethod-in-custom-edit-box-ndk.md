---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/use-inputmethod-in-custom-edit-box-ndk
title: 在自绘编辑框中使用输入法开发指导 (C/C++)
breadcrumb: 指南 > 应用框架 > IME Kit（输入法开发服务） > 在自绘编辑框中使用输入法开发指导 (C/C++)
category: harmonyos-guides
scraped_at: 2026-04-28T07:41:38+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:95be14c23dbc22d45e5c870c6bf69f1f075cb850af8693dbec1143704ac79242
---

## 场景介绍

IME Kit支持开发者在自绘编辑框中使用输入法，与输入法应用交互，包括显示、隐藏输入法，接收来自输入法应用的文本编辑操作通知等，本文档介绍开发者如何使用C/C++完成此功能开发。

## 接口说明

详细接口说明请参考[InputMethod接口文档](../harmonyos-references/capi-inputmethod.md)。

## 添加动态链接库

CMakeLists.txt中添加以下lib。

```
1. libohinputmethod.so
```

## 引用头文件

```
1. #include <inputmethod/inputmethod_controller_capi.h>
```

## 绑定输入法

开发者需要在输入框获焦时，通过调用接口[OH\_InputMethodController\_Attach](../harmonyos-references/capi-inputmethod-controller-capi-h.md#oh_inputmethodcontroller_attach)绑定输入法，绑定成功后用户可以通过输入法输入文字。

1. 创建InputMethod\_TextEditorProxy实例，示例代码如下所示：

   ```
   1. // 创建InputMethod_TextEditorProxy实例
   2. textEditorProxy = OH_TextEditorProxy_Create();
   ```

   [napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/InputMethod/KikaInputMethod/entry/src/main/cpp/napi_init.cpp#L211-L214)
2. 创建InputMethod\_AttachOptions实例，设置绑定输入法时的选项。示例代码如下所示：

   ```
   1. // 创建InputMethod_AttachOptions实例，选项showKeyboard用于指定此次绑定成功后是否显示键盘，此处以目标显示键盘为例
   2. bool showKeyboard = true;
   3. attachOptions = OH_AttachOptions_Create(showKeyboard);
   ```

   [napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/InputMethod/KikaInputMethod/entry/src/main/cpp/napi_init.cpp#L223-L227)
3. 调用OH\_InputMethodController\_Attach发起绑定输入法服务，调用成功后，可以获取到用于和输入法交互的InputMethod\_InputMethodProxy。示例代码如下所示：

   ```
   1. // 发起绑定请求
   2. auto ret = OH_InputMethodController_Attach(textEditorProxy, attachOptions, &inputMethodProxy);
   3. if (ret != IME_ERR_OK) {
   4. OH_LOG_Print(LOG_APP, LOG_ERROR, 0, "testTag", "Attach failed, ret=%{public}d.", ret);
   5. OH_TextEditorProxy_Destroy(textEditorProxy);
   6. OH_AttachOptions_Destroy(attachOptions);
   7. return;
   8. }
   ```

   [napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/InputMethod/KikaInputMethod/entry/src/main/cpp/napi_init.cpp#L234-L243)

## 显示/隐藏面板功能

绑定成功后，可以使用获取到的[InputMethod\_InputMethodProxy](../harmonyos-references/capi-inputmethod-inputmethod-inputmethodproxy.md)对象向输入法发送消息。示例代码如下所示：

```
1. // 显示键盘
2. if (OH_InputMethodProxy_ShowKeyboard(inputMethodProxy) != InputMethod_ErrorCode::IME_ERR_OK) {
3. OH_LOG_Print(LOG_APP, LOG_ERROR, 0, "testTag", "ShowKeyboard failed!");
4. }
5. // 隐藏键盘
6. if (OH_InputMethodProxy_HideKeyboard(inputMethodProxy) != InputMethod_ErrorCode::IME_ERR_OK) {
7. OH_LOG_Print(LOG_APP, LOG_ERROR, 0, "testTag", "HideKeyboard failed!");
8. }
9. // 通知输入框配置信息变化
10. if (OH_InputMethodProxy_NotifyConfigurationChange(inputMethodProxy, InputMethod_EnterKeyType::IME_ENTER_KEY_GO, InputMethod_TextInputType::IME_TEXT_INPUT_TYPE_TEXT) != InputMethod_ErrorCode::IME_ERR_OK) {
11. OH_LOG_Print(LOG_APP, LOG_ERROR, 0, "testTag", "NotifyConfigurationChange failed!");
12. }
```

## 监听输入法应用的请求/通知

1. 需要先实现对输入法应用发送的请求或通知的响应处理函数，示例代码如下所示：

   ```
   1. // 实现InputMethod_TextEditorProxy中的输入法应用事件响应函数
   2. void GetTextConfig(InputMethod_TextEditorProxy *textEditorProxy, InputMethod_TextConfig *config)
   3. {
   4. // 处理输入法发送的获取输入框配置请求
   5. }
   6. void InsertText(InputMethod_TextEditorProxy *textEditorProxy, const char16_t *text, size_t length)
   7. {
   8. // 处理输入法发送的插入文本请求
   9. }
   10. void DeleteForward(InputMethod_TextEditorProxy *textEditorProxy, int32_t length)
   11. {
   12. // 处理输入法发送的删除文本请求
   13. }
   14. // ......
   ```
2. 将实现后的响应函数，设置到[InputMethod\_TextEditorProxy](../harmonyos-references/capi-inputmethod-inputmethod-texteditorproxy.md)中，再通过绑定输入法时调用的[OH\_InputMethodController\_Attach](../harmonyos-references/capi-inputmethod-controller-capi-h.md#oh_inputmethodcontroller_attach)将其设置到输入法框架中，完成监听注册。示例代码如下所示：

   ```
   1. OH_TextEditorProxy_SetGetTextConfigFunc(textEditorProxy, GetTextConfigFunc);
   2. OH_TextEditorProxy_SetInsertTextFunc(textEditorProxy, InsertTextFunc);
   3. OH_TextEditorProxy_SetDeleteForwardFunc(textEditorProxy, DeleteForwardFunc);
   4. OH_TextEditorProxy_SetDeleteBackwardFunc(textEditorProxy, DeleteBackwardFunc);
   5. OH_TextEditorProxy_SetSendKeyboardStatusFunc(textEditorProxy, SendKeyboardStatusFunc);
   6. OH_TextEditorProxy_SetSendEnterKeyFunc(textEditorProxy, SendEnterKeyFunc);
   7. OH_TextEditorProxy_SetMoveCursorFunc(textEditorProxy, MoveCursorFunc);
   8. OH_TextEditorProxy_SetHandleSetSelectionFunc(textEditorProxy, HandleSetSelectionFunc);
   9. OH_TextEditorProxy_SetHandleExtendActionFunc(textEditorProxy, HandleExtendActionFunc);
   10. OH_TextEditorProxy_SetGetLeftTextOfCursorFunc(textEditorProxy, GetLeftTextOfCursorFunc);
   11. OH_TextEditorProxy_SetGetRightTextOfCursorFunc(textEditorProxy, GetRightTextOfCursorFunc);
   12. OH_TextEditorProxy_SetGetTextIndexAtCursorFunc(textEditorProxy, GetTextIndexAtCursorFunc);
   13. OH_TextEditorProxy_SetReceivePrivateCommandFunc(textEditorProxy, ReceivePrivateCommandFunc);
   14. OH_TextEditorProxy_SetSetPreviewTextFunc(textEditorProxy, SetPreviewTextFunc);
   15. OH_TextEditorProxy_SetFinishTextPreviewFunc(textEditorProxy, FinishTextPreviewFunc);
   ```

   [napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/InputMethod/KikaInputMethod/entry/src/main/cpp/napi_init.cpp#L188-L204)

## 解绑输入法

当编辑框失焦，需要结束使用输入法，通过接口[OH\_InputMethodController\_Detach](../harmonyos-references/capi-inputmethod-controller-capi-h.md#oh_inputmethodcontroller_detach)与输入法框架解绑。

```
1. // 发起解绑请求
2. OH_InputMethodController_Detach(inputMethodProxy);
3. OH_TextEditorProxy_Destroy(textEditorProxy);
4. OH_AttachOptions_Destroy(attachOptions);
```

[napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/InputMethod/KikaInputMethod/entry/src/main/cpp/napi_init.cpp#L257-L262)

## 完整示例

示例代码展示了绑定输入法、隐藏输入法、解绑输入法的完整流程。

示例代码总入口为InputMethodNdkDemo函数。

说明：

需要在CMakeList.txt中添加libohinputmethod.so libhilog\_ndk.z.so依赖。

```
1. #include "napi/native_api.h"
2. #include <codecvt>
3. #include <locale>
4. #include <thread>

6. #include "hilog/log.h"
7. #include "inputmethod/inputmethod_controller_capi.h"

9. constexpr int32_t TEXTSIZE = 1024;

11. static std::string g_strText;
12. char g_strTextChar[TEXTSIZE];
13. int32_t g_strTextCharLen = 0;
14. bool g_flagShow = false;
15. std::mutex g_textMutex;
16. InputMethod_TextEditorProxy *textEditorProxy = nullptr;
17. InputMethod_AttachOptions *attachOptions = nullptr;
18. InputMethod_InputMethodProxy *inputMethodProxy = nullptr;

20. void InputMethodDestroy();

22. void InitText()
23. {
24. std::lock_guard<std::mutex> lock(g_textMutex);
25. if (g_flagShow) {
26. memset(g_strTextChar, 0x00, sizeof(g_strTextChar));
27. g_strTextCharLen = 0;
28. g_flagShow = false;
29. }
30. }

32. void SetText(const char* input)
33. {
34. std::lock_guard<std::mutex> lock(g_textMutex);
35. g_strTextCharLen = strlen(input);
36. if (g_strTextCharLen > TEXTSIZE) {
37. OH_LOG_Print(LOG_APP, LOG_ERROR, 0, "testTag", "Length greater than 1024 , ret=%{public}d", g_strTextCharLen);
38. }
39. strncpy(g_strTextChar, input, g_strTextCharLen);
40. }

42. void GetTextConfigFunc(InputMethod_TextEditorProxy *proxy, InputMethod_TextConfig *config)
43. { // 处理获取输入框配置请求
44. auto ret = OH_TextConfig_SetEnterKeyType(config, InputMethod_EnterKeyType::IME_ENTER_KEY_SEND);
45. if (ret != IME_ERR_OK) {
46. OH_LOG_Print(LOG_APP, LOG_ERROR, 0, "testTag", "SetEnterKeyType failed, ret=%{public}d", ret);
47. return;
48. }

50. ret = OH_TextConfig_SetInputType(config, InputMethod_TextInputType::IME_TEXT_INPUT_TYPE_PHONE);
51. if (ret != IME_ERR_OK) {
52. OH_LOG_Print(LOG_APP, LOG_ERROR, 0, "testTag", "SetInputType failed, ret=%{public}d", ret);
53. return;
54. }
55. }

57. void InsertTextFunc(InputMethod_TextEditorProxy *proxy, const char16_t *text, size_t length)
58. {
59. InitText();

61. // 处理插入文本请求
62. // 将char16_t类型的字符串转换为u16string
63. std::u16string u16Str(text, length + 1);

65. // 转换为UTF-8编码的string
66. std::wstring_convert<std::codecvt_utf8_utf16<char16_t>, char16_t> converter;
67. std::string utf8Str = converter.to_bytes(u16Str);
68. for (size_t i = 0; i < utf8Str.size(); ++i) {
69. unsigned char c = static_cast<unsigned char>(utf8Str[i]);
70. if (c != 0x00) {
71. std::lock_guard<std::mutex> lock(g_textMutex);
72. g_strTextChar[g_strTextCharLen] = c;
73. g_strTextCharLen += 1;
74. }
75. }
76. }

78. void DeleteForwardFunc(InputMethod_TextEditorProxy *proxy, int32_t length)
79. {
80. std::lock_guard<std::mutex> lock(g_textMutex);
81. if (g_strTextCharLen > 0) {
82. strncpy(g_strTextChar, g_strTextChar + 1, g_strTextCharLen - 1);
83. g_strTextCharLen = (g_strTextCharLen > 0) ? g_strTextCharLen - 1 : g_strTextCharLen;
84. }
85. }

87. void DeleteBackwardFunc(InputMethod_TextEditorProxy *proxy, int32_t length)
88. {
89. std::lock_guard<std::mutex> lock(g_textMutex);
90. g_strTextCharLen = (g_strTextCharLen > 0) ? g_strTextCharLen - 1 : g_strTextCharLen;
91. g_strTextChar[g_strTextCharLen] = '\0';
92. }

94. void SendKeyboardStatusFunc(InputMethod_TextEditorProxy *proxy, InputMethod_KeyboardStatus status)
95. {
96. if (status == InputMethod_KeyboardStatus::IME_KEYBOARD_STATUS_HIDE) {
97. g_flagShow = false;
98. SetText("键盘已经被隐藏");
99. } else if (status == InputMethod_KeyboardStatus::IME_KEYBOARD_STATUS_SHOW && g_flagShow != true) {
100. g_flagShow = true;
101. SetText("键盘已经被拉起");
102. }
103. }

105. void SendEnterKeyFunc(InputMethod_TextEditorProxy *proxy, InputMethod_EnterKeyType type)
106. {
107. SetText("处理回车键请求事件");
108. g_flagShow = true;
109. }

111. void MoveCursorFunc(InputMethod_TextEditorProxy *proxy, InputMethod_Direction direction)
112. {
113. if (direction == InputMethod_Direction::IME_DIRECTION_UP) {
114. SetText("光标正在向 上 移动");
115. } else if (direction == InputMethod_Direction::IME_DIRECTION_DOWN) {
116. SetText("光标正在向 下 移动");
117. } else if (direction == InputMethod_Direction::IME_DIRECTION_LEFT) {
118. SetText("光标正在向 左 移动");
119. } else if (direction == InputMethod_Direction::IME_DIRECTION_RIGHT) {
120. SetText("光标正在向 右  移动");
121. } else {
122. SetText("光标移动 出现错误");
123. }
124. }

126. void HandleSetSelectionFunc(InputMethod_TextEditorProxy *proxy, int32_t start, int32_t end)
127. {
128. SetText("处理选中文本请求");
129. }

131. void HandleExtendActionFunc(InputMethod_TextEditorProxy *proxy, InputMethod_ExtendAction action)
132. {
133. SetText("处理扩展编辑请求");
134. }

136. void GetLeftTextOfCursorFunc(InputMethod_TextEditorProxy *proxy, int32_t number, char16_t text[], size_t *length)
137. {
138. OH_LOG_Print(LOG_APP, LOG_INFO, 0, "testTag", "处理获取光标左侧文本请求  ...");
139. }

141. void GetRightTextOfCursorFunc(InputMethod_TextEditorProxy *proxy, int32_t number, char16_t text[], size_t *length)
142. {
143. OH_LOG_Print(LOG_APP, LOG_INFO, 0, "testTag", "处理获取光标右侧文本请求  ...");
144. }

146. int32_t GetTextIndexAtCursorFunc(InputMethod_TextEditorProxy *proxy)
147. {
148. OH_LOG_Print(LOG_APP, LOG_INFO, 0, "testTag", "处理获取光标所在输入框文本索引请求  ...");
149. return 0;
150. }
151. int32_t ReceivePrivateCommandFunc(InputMethod_TextEditorProxy *proxy, InputMethod_PrivateCommand *privateCommand[],
152. size_t size)
153. {
154. SetText("处理扩展编辑请求");
155. return 0;
156. }

158. int32_t SetPreviewTextFunc(InputMethod_TextEditorProxy *proxy, const char16_t *text, size_t length, int32_t start,
159. int32_t end)
160. {
161. SetText("处理设置预上屏文本请求");
162. return 0;
163. }

165. void FinishTextPreviewFunc(InputMethod_TextEditorProxy *proxy)
166. {
167. SetText("处理结束预上屏请求");
168. }

170. void ConstructTextEditorProxy(InputMethod_TextEditorProxy *textEditorProxy)
171. {
172. OH_TextEditorProxy_SetGetTextConfigFunc(textEditorProxy, GetTextConfigFunc);
173. OH_TextEditorProxy_SetInsertTextFunc(textEditorProxy, InsertTextFunc);
174. OH_TextEditorProxy_SetDeleteForwardFunc(textEditorProxy, DeleteForwardFunc);
175. OH_TextEditorProxy_SetDeleteBackwardFunc(textEditorProxy, DeleteBackwardFunc);
176. OH_TextEditorProxy_SetSendKeyboardStatusFunc(textEditorProxy, SendKeyboardStatusFunc);
177. OH_TextEditorProxy_SetSendEnterKeyFunc(textEditorProxy, SendEnterKeyFunc);
178. OH_TextEditorProxy_SetMoveCursorFunc(textEditorProxy, MoveCursorFunc);
179. OH_TextEditorProxy_SetHandleSetSelectionFunc(textEditorProxy, HandleSetSelectionFunc);
180. OH_TextEditorProxy_SetHandleExtendActionFunc(textEditorProxy, HandleExtendActionFunc);
181. OH_TextEditorProxy_SetGetLeftTextOfCursorFunc(textEditorProxy, GetLeftTextOfCursorFunc);
182. OH_TextEditorProxy_SetGetRightTextOfCursorFunc(textEditorProxy, GetRightTextOfCursorFunc);
183. OH_TextEditorProxy_SetGetTextIndexAtCursorFunc(textEditorProxy, GetTextIndexAtCursorFunc);
184. OH_TextEditorProxy_SetReceivePrivateCommandFunc(textEditorProxy, ReceivePrivateCommandFunc);
185. OH_TextEditorProxy_SetSetPreviewTextFunc(textEditorProxy, SetPreviewTextFunc);
186. OH_TextEditorProxy_SetFinishTextPreviewFunc(textEditorProxy, FinishTextPreviewFunc);
187. }
```

[napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/InputMethod/KikaInputMethod/entry/src/main/cpp/napi_init.cpp#L16-L206)

```
1. void InputMethodNdkDemo()
2. {
3. // 创建InputMethod_TextEditorProxy实例
4. textEditorProxy = OH_TextEditorProxy_Create();
5. if (textEditorProxy == nullptr) {
6. OH_LOG_Print(LOG_APP, LOG_ERROR, 0, "testTag", "Create TextEditorProxy failed.");
7. return;
8. }

10. // 将实现好的响应处理函数设置到InputMethod_TextEditorProxy中
11. ConstructTextEditorProxy(textEditorProxy);

13. // 创建InputMethod_AttachOptions实例，选项showKeyboard用于指定此次绑定成功后是否显示键盘，此处以目标显示键盘为例
14. bool showKeyboard = true;
15. attachOptions = OH_AttachOptions_Create(showKeyboard);
16. if (attachOptions == nullptr) {
17. OH_LOG_Print(LOG_APP, LOG_ERROR, 0, "testTag", "Create AttachOptions failed.");
18. OH_TextEditorProxy_Destroy(textEditorProxy);
19. return;
20. }

22. // 发起绑定请求
23. auto ret = OH_InputMethodController_Attach(textEditorProxy, attachOptions, &inputMethodProxy);
24. if (ret != IME_ERR_OK) {
25. OH_LOG_Print(LOG_APP, LOG_ERROR, 0, "testTag", "Attach failed, ret=%{public}d.", ret);
26. OH_TextEditorProxy_Destroy(textEditorProxy);
27. OH_AttachOptions_Destroy(attachOptions);
28. return;
29. }
30. }

32. static napi_value InputMethodDestroy(napi_env env, napi_callback_info info)
33. {
34. // 隐藏键盘
35. int ret = OH_InputMethodProxy_HideKeyboard(inputMethodProxy);
36. if (ret != IME_ERR_OK) {
37. OH_LOG_Print(LOG_APP, LOG_ERROR, 0, "testTag", "HideKeyboard failed, ret=%{public}d.", ret);
38. OH_TextEditorProxy_Destroy(textEditorProxy);
39. OH_AttachOptions_Destroy(attachOptions);
40. return nullptr;
41. }

43. // 发起解绑请求
44. OH_InputMethodController_Detach(inputMethodProxy);
45. OH_TextEditorProxy_Destroy(textEditorProxy);
46. OH_AttachOptions_Destroy(attachOptions);
47. OH_LOG_Print(LOG_APP, LOG_INFO, 0, "testTag", "Finished.");
48. return nullptr;
49. }

52. static napi_value AttachInputMethod(napi_env env, napi_callback_info info)
53. {
54. InputMethodNdkDemo();

56. napi_value result;
57. napi_create_string_utf8(env,  g_strText.c_str(),  g_strText.length(),  &result);
58. return result;
59. }

61. static napi_value GetText(napi_env env, napi_callback_info info)
62. {
63. napi_value result;
64. napi_create_string_utf8(env, g_strTextChar, g_strTextCharLen,  &result);
65. return result;
66. }

68. EXTERN_C_START
69. static napi_value Init(napi_env env, napi_value exports)
70. {
71. napi_property_descriptor desc[] = {
72. { "attachInputMethod", nullptr, AttachInputMethod, nullptr, nullptr, nullptr, napi_default, nullptr },
73. { "getText", nullptr, GetText, nullptr, nullptr, nullptr, napi_default, nullptr },
74. { "inputMethodDestroy", nullptr, InputMethodDestroy, nullptr, nullptr, nullptr, napi_default, nullptr },
75. };
76. napi_define_properties(env, exports, sizeof(desc) / sizeof(desc[0]), desc);
77. return exports;
78. }
79. EXTERN_C_END

81. static napi_module demoModule = {
82. .nm_version = 1,
83. .nm_flags = 0,
84. .nm_filename = nullptr,
85. .nm_register_func = Init,
86. .nm_modname = "entry",
87. .nm_priv = ((void*)0),
88. .reserved = { 0 },
89. };

91. extern "C" __attribute__((constructor)) void RegisterEntryModule(void)
92. {
93. napi_module_register(&demoModule);
94. }
```

[napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/InputMethod/KikaInputMethod/entry/src/main/cpp/napi_init.cpp#L208-L311)
