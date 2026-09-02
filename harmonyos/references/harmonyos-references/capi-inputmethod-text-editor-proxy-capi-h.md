---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-inputmethod-text-editor-proxy-capi-h
title: inputmethod_text_editor_proxy_capi.h
breadcrumb: API参考 > 应用框架 > IME Kit（输入法开发服务） > C API > 头文件 > inputmethod_text_editor_proxy_capi.h
category: harmonyos-references
scraped_at: 2026-09-02T15:01:36+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:58e91974ea99a70e544bd415b6316db99afab54ad3812ac2772125edc6bdbdb0
---

## 概述

提供一套方法支持应用开发的自绘输入框获取来自输入法应用的通知和请求。该模块采用回调机制实现输入法应用与自绘输入框之间的双向通信。

**引用文件：** <inputmethod/inputmethod\_text\_editor\_proxy\_capi.h>

**库：** libohinputmethod.so

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**起始版本：** 12

**相关模块：** [InputMethod](capi-inputmethod.md)

## 汇总

### 结构体

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md) | InputMethod\_TextEditorProxy | 输入法文本编辑器代理类。提供了获取来自输入法应用的通知和请求的方法。 |

### 函数

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [typedef void (\*OH\_TextEditorProxy\_GetTextConfigFunc)(InputMethod\_TextEditorProxy \*textEditorProxy, InputMethod\_TextConfig \*config)](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_gettextconfigfunc) | OH\_TextEditorProxy\_GetTextConfigFunc | 输入法获取输入框配置时触发的函数。 |
| [typedef void (\*OH\_TextEditorProxy\_InsertTextFunc)(InputMethod\_TextEditorProxy \*textEditorProxy, const char16\_t \*text, size\_t length)](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_inserttextfunc) | OH\_TextEditorProxy\_InsertTextFunc | 输入法应用插入文本时触发的函数。 |
| [typedef void (\*OH\_TextEditorProxy\_DeleteForwardFunc)(InputMethod\_TextEditorProxy \*textEditorProxy, int32\_t length)](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_deleteforwardfunc) | OH\_TextEditorProxy\_DeleteForwardFunc | 输入法删除光标右侧文本时触发的函数。 |
| [typedef void (\*OH\_TextEditorProxy\_DeleteBackwardFunc)(InputMethod\_TextEditorProxy \*textEditorProxy, int32\_t length)](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_deletebackwardfunc) | OH\_TextEditorProxy\_DeleteBackwardFunc | 输入法删除光标左侧文本时触发的函数。 |
| [typedef void (\*OH\_TextEditorProxy\_SendKeyboardStatusFunc)(InputMethod\_TextEditorProxy \*textEditorProxy, InputMethod\_KeyboardStatus keyboardStatus)](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_sendkeyboardstatusfunc) | OH\_TextEditorProxy\_SendKeyboardStatusFunc | 输入法通知键盘状态时触发的函数。 |
| [typedef void (\*OH\_TextEditorProxy\_SendEnterKeyFunc)(InputMethod\_TextEditorProxy \*textEditorProxy, InputMethod\_EnterKeyType enterKeyType)](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_sendenterkeyfunc) | OH\_TextEditorProxy\_SendEnterKeyFunc | 输入法发送回车键时触发的函数。 |
| [typedef void (\*OH\_TextEditorProxy\_MoveCursorFunc)(InputMethod\_TextEditorProxy \*textEditorProxy, InputMethod\_Direction direction)](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_movecursorfunc) | OH\_TextEditorProxy\_MoveCursorFunc | 输入法移动光标时触发的函数。 |
| [typedef void (\*OH\_TextEditorProxy\_HandleSetSelectionFunc)(InputMethod\_TextEditorProxy \*textEditorProxy, int32\_t start, int32\_t end)](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_handlesetselectionfunc) | OH\_TextEditorProxy\_HandleSetSelectionFunc | 输入法请求选中文本时触发的函数。 |
| [typedef void (\*OH\_TextEditorProxy\_HandleExtendActionFunc)(InputMethod\_TextEditorProxy \*textEditorProxy, InputMethod\_ExtendAction action)](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_handleextendactionfunc) | OH\_TextEditorProxy\_HandleExtendActionFunc | 输入法发送扩展编辑操作时触发的函数。 |
| [typedef void (\*OH\_TextEditorProxy\_GetLeftTextOfCursorFunc)(InputMethod\_TextEditorProxy \*textEditorProxy, int32\_t number, char16\_t text[], size\_t \*length)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-inputmethod-text-editor-proxy-capi-h#oh_texteditorproxy_getlefttextofcursorfunc) | OH\_TextEditorProxy\_GetLeftTextOfCursorFunc | 输入法获取光标左侧文本时触发的函数。 |
| [typedef void (\*OH\_TextEditorProxy\_GetRightTextOfCursorFunc)(InputMethod\_TextEditorProxy \*textEditorProxy, int32\_t number, char16\_t text[], size\_t \*length)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-inputmethod-text-editor-proxy-capi-h#oh_texteditorproxy_getrighttextofcursorfunc) | OH\_TextEditorProxy\_GetRightTextOfCursorFunc | 输入法获取光标右侧文本时触发的函数。 |
| [typedef int32\_t (\*OH\_TextEditorProxy\_GetTextIndexAtCursorFunc)(InputMethod\_TextEditorProxy \*textEditorProxy)](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_gettextindexatcursorfunc) | OH\_TextEditorProxy\_GetTextIndexAtCursorFunc | 输入法获取光标所在输入框文本索引时触发的函数。 |
| [typedef int32\_t (\*OH\_TextEditorProxy\_ReceivePrivateCommandFunc)(InputMethod\_TextEditorProxy \*textEditorProxy, InputMethod\_PrivateCommand \*privateCommand[], size\_t size)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-inputmethod-text-editor-proxy-capi-h#oh_texteditorproxy_receiveprivatecommandfunc) | OH\_TextEditorProxy\_ReceivePrivateCommandFunc | 输入法应用发送私有数据命令时触发的函数。 |
| [typedef int32\_t (\*OH\_TextEditorProxy\_SetPreviewTextFunc)(InputMethod\_TextEditorProxy \*textEditorProxy, const char16\_t text[], size\_t length, int32\_t start, int32\_t end)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-inputmethod-text-editor-proxy-capi-h#oh_texteditorproxy_setpreviewtextfunc) | OH\_TextEditorProxy\_SetPreviewTextFunc | 输入法设置预上屏文本时触发的函数。 |
| [typedef void (\*OH\_TextEditorProxy\_FinishTextPreviewFunc)(InputMethod\_TextEditorProxy \*textEditorProxy)](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_finishtextpreviewfunc) | OH\_TextEditorProxy\_FinishTextPreviewFunc | 输入法结束预上屏时触发的函数。 |
| [InputMethod\_TextEditorProxy \*OH\_TextEditorProxy\_Create(void)](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_create) | - | 创建一个新的InputMethod\_TextEditorProxy实例。 |
| [void OH\_TextEditorProxy\_Destroy(InputMethod\_TextEditorProxy \*proxy)](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_destroy) | - | 销毁一个InputMethod\_TextEditorProxy实例。 |
| [InputMethod\_ErrorCode OH\_TextEditorProxy\_SetGetTextConfigFunc(InputMethod\_TextEditorProxy \*proxy, OH\_TextEditorProxy\_GetTextConfigFunc getTextConfigFunc)](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_setgettextconfigfunc) | - | 将GetTextConfigFunc设置到TextEditorProxy中。 |
| [InputMethod\_ErrorCode OH\_TextEditorProxy\_SetInsertTextFunc(InputMethod\_TextEditorProxy \*proxy, OH\_TextEditorProxy\_InsertTextFunc insertTextFunc)](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_setinserttextfunc) | - | 将InsertTextFunc设置到TextEditorProxy中。 |
| [InputMethod\_ErrorCode OH\_TextEditorProxy\_SetDeleteForwardFunc(InputMethod\_TextEditorProxy \*proxy, OH\_TextEditorProxy\_DeleteForwardFunc deleteForwardFunc)](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_setdeleteforwardfunc) | - | 将DeleteForwardFunc设置到TextEditorProxy中。 |
| [InputMethod\_ErrorCode OH\_TextEditorProxy\_SetDeleteBackwardFunc(InputMethod\_TextEditorProxy \*proxy, OH\_TextEditorProxy\_DeleteBackwardFunc deleteBackwardFunc)](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_setdeletebackwardfunc) | - | 将DeleteBackwardFunc设置到TextEditorProxy中。 |
| [InputMethod\_ErrorCode OH\_TextEditorProxy\_SetSendKeyboardStatusFunc(InputMethod\_TextEditorProxy \*proxy, OH\_TextEditorProxy\_SendKeyboardStatusFunc sendKeyboardStatusFunc)](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_setsendkeyboardstatusfunc) | - | 将SendKeyboardStatusFunc设置到TextEditorProxy中。 |
| [InputMethod\_ErrorCode OH\_TextEditorProxy\_SetSendEnterKeyFunc(InputMethod\_TextEditorProxy \*proxy, OH\_TextEditorProxy\_SendEnterKeyFunc sendEnterKeyFunc)](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_setsendenterkeyfunc) | - | 将SendEnterKeyFunc设置到TextEditorProxy中。 |
| [InputMethod\_ErrorCode OH\_TextEditorProxy\_SetMoveCursorFunc(InputMethod\_TextEditorProxy \*proxy, OH\_TextEditorProxy\_MoveCursorFunc moveCursorFunc)](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_setmovecursorfunc) | - | 将MoveCursorFunc设置到TextEditorProxy中。 |
| [InputMethod\_ErrorCode OH\_TextEditorProxy\_SetHandleSetSelectionFunc(InputMethod\_TextEditorProxy \*proxy, OH\_TextEditorProxy\_HandleSetSelectionFunc handleSetSelectionFunc)](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_sethandlesetselectionfunc) | - | 将HandleSetSelectionFunc设置到TextEditorProxy中。 |
| [InputMethod\_ErrorCode OH\_TextEditorProxy\_SetHandleExtendActionFunc(InputMethod\_TextEditorProxy \*proxy, OH\_TextEditorProxy\_HandleExtendActionFunc handleExtendActionFunc)](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_sethandleextendactionfunc) | - | 将HandleExtendActionFunc设置到TextEditorProxy中。 |
| [InputMethod\_ErrorCode OH\_TextEditorProxy\_SetGetLeftTextOfCursorFunc(InputMethod\_TextEditorProxy \*proxy, OH\_TextEditorProxy\_GetLeftTextOfCursorFunc getLeftTextOfCursorFunc)](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_setgetlefttextofcursorfunc) | - | 将GetLeftTextOfCursorFunc设置到TextEditorProxy中。 |
| [InputMethod\_ErrorCode OH\_TextEditorProxy\_SetGetRightTextOfCursorFunc(InputMethod\_TextEditorProxy \*proxy, OH\_TextEditorProxy\_GetRightTextOfCursorFunc getRightTextOfCursorFunc)](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_setgetrighttextofcursorfunc) | - | 将GetRightTextOfCursorFunc设置到TextEditorProxy中。 |
| [InputMethod\_ErrorCode OH\_TextEditorProxy\_SetGetTextIndexAtCursorFunc(InputMethod\_TextEditorProxy \*proxy, OH\_TextEditorProxy\_GetTextIndexAtCursorFunc getTextIndexAtCursorFunc)](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_setgettextindexatcursorfunc) | - | 将GetTextIndexAtCursorFunc设置到TextEditorProxy中。 |
| [InputMethod\_ErrorCode OH\_TextEditorProxy\_SetReceivePrivateCommandFunc(InputMethod\_TextEditorProxy \*proxy, OH\_TextEditorProxy\_ReceivePrivateCommandFunc receivePrivateCommandFunc)](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_setreceiveprivatecommandfunc) | - | 将ReceivePrivateCommandFunc设置到TextEditorProxy中。 |
| [InputMethod\_ErrorCode OH\_TextEditorProxy\_SetSetPreviewTextFunc(InputMethod\_TextEditorProxy \*proxy, OH\_TextEditorProxy\_SetPreviewTextFunc setPreviewTextFunc)](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_setsetpreviewtextfunc) | - | 将SetPreviewTextFunc设置到TextEditorProxy中。 |
| [InputMethod\_ErrorCode OH\_TextEditorProxy\_SetFinishTextPreviewFunc(InputMethod\_TextEditorProxy \*proxy, OH\_TextEditorProxy\_FinishTextPreviewFunc finishTextPreviewFunc)](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_setfinishtextpreviewfunc) | - | 将FinishTextPreviewFunc设置到TextEditorProxy中。 |
| [InputMethod\_ErrorCode OH\_TextEditorProxy\_GetGetTextConfigFunc(InputMethod\_TextEditorProxy \*proxy, OH\_TextEditorProxy\_GetTextConfigFunc \*getTextConfigFunc)](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_getgettextconfigfunc) | - | 从TextEditorProxy中获取GetTextConfigFunc函数。 |
| [InputMethod\_ErrorCode OH\_TextEditorProxy\_GetInsertTextFunc(InputMethod\_TextEditorProxy \*proxy, OH\_TextEditorProxy\_InsertTextFunc \*insertTextFunc)](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_getinserttextfunc) | - | 从TextEditorProxy中获取InsertTextFunc函数。 |
| [InputMethod\_ErrorCode OH\_TextEditorProxy\_GetDeleteForwardFunc(InputMethod\_TextEditorProxy \*proxy, OH\_TextEditorProxy\_DeleteForwardFunc \*deleteForwardFunc)](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_getdeleteforwardfunc) | - | 从TextEditorProxy中获取DeleteForwardFunc函数。 |
| [InputMethod\_ErrorCode OH\_TextEditorProxy\_GetDeleteBackwardFunc(InputMethod\_TextEditorProxy \*proxy, OH\_TextEditorProxy\_DeleteBackwardFunc \*deleteBackwardFunc)](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_getdeletebackwardfunc) | - | 从TextEditorProxy中获取DeleteBackwardFunc函数。 |
| [InputMethod\_ErrorCode OH\_TextEditorProxy\_GetSendKeyboardStatusFunc(InputMethod\_TextEditorProxy \*proxy, OH\_TextEditorProxy\_SendKeyboardStatusFunc \*sendKeyboardStatusFunc)](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_getsendkeyboardstatusfunc) | - | 从TextEditorProxy中获取SendKeyboardStatusFunc函数。 |
| [InputMethod\_ErrorCode OH\_TextEditorProxy\_GetSendEnterKeyFunc(InputMethod\_TextEditorProxy \*proxy, OH\_TextEditorProxy\_SendEnterKeyFunc \*sendEnterKeyFunc)](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_getsendenterkeyfunc) | - | 从TextEditorProxy中获取SendEnterKeyFunc函数。 |
| [InputMethod\_ErrorCode OH\_TextEditorProxy\_GetMoveCursorFunc(InputMethod\_TextEditorProxy \*proxy, OH\_TextEditorProxy\_MoveCursorFunc \*moveCursorFunc)](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_getmovecursorfunc) | - | 从TextEditorProxy中获取MoveCursorFunc函数。 |
| [InputMethod\_ErrorCode OH\_TextEditorProxy\_GetHandleSetSelectionFunc(InputMethod\_TextEditorProxy \*proxy, OH\_TextEditorProxy\_HandleSetSelectionFunc \*handleSetSelectionFunc)](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_gethandlesetselectionfunc) | - | 从TextEditorProxy中获取HandleSetSelectionFunc函数。 |
| [InputMethod\_ErrorCode OH\_TextEditorProxy\_GetHandleExtendActionFunc(InputMethod\_TextEditorProxy \*proxy, OH\_TextEditorProxy\_HandleExtendActionFunc \*handleExtendActionFunc)](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_gethandleextendactionfunc) | - | 从TextEditorProxy中获取HandleExtendActionFunc函数。 |
| [InputMethod\_ErrorCode OH\_TextEditorProxy\_GetGetLeftTextOfCursorFunc(InputMethod\_TextEditorProxy \*proxy, OH\_TextEditorProxy\_GetLeftTextOfCursorFunc \*getLeftTextOfCursorFunc)](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_getgetlefttextofcursorfunc) | - | 从TextEditorProxy中获取GetLeftTextOfCursorFunc函数。 |
| [InputMethod\_ErrorCode OH\_TextEditorProxy\_GetGetRightTextOfCursorFunc(InputMethod\_TextEditorProxy \*proxy, OH\_TextEditorProxy\_GetRightTextOfCursorFunc \*getRightTextOfCursorFunc)](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_getgetrighttextofcursorfunc) | - | 从TextEditorProxy中获取GetRightTextOfCursorFunc函数。 |
| [InputMethod\_ErrorCode OH\_TextEditorProxy\_GetGetTextIndexAtCursorFunc(InputMethod\_TextEditorProxy \*proxy, OH\_TextEditorProxy\_GetTextIndexAtCursorFunc \*getTextIndexAtCursorFunc)](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_getgettextindexatcursorfunc) | - | 从TextEditorProxy中获取GetTextIndexAtCursorFunc函数。 |
| [InputMethod\_ErrorCode OH\_TextEditorProxy\_GetReceivePrivateCommandFunc(InputMethod\_TextEditorProxy \*proxy, OH\_TextEditorProxy\_ReceivePrivateCommandFunc \*receivePrivateCommandFunc)](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_getreceiveprivatecommandfunc) | - | 从TextEditorProxy中获取ReceivePrivateCommandFunc函数。 |
| [InputMethod\_ErrorCode OH\_TextEditorProxy\_GetSetPreviewTextFunc(InputMethod\_TextEditorProxy \*proxy, OH\_TextEditorProxy\_SetPreviewTextFunc \*setPreviewTextFunc)](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_getsetpreviewtextfunc) | - | 从TextEditorProxy中获取SetPreviewTextFunc函数。 |
| [InputMethod\_ErrorCode OH\_TextEditorProxy\_GetFinishTextPreviewFunc(InputMethod\_TextEditorProxy \*proxy, OH\_TextEditorProxy\_FinishTextPreviewFunc \*finishTextPreviewFunc)](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_getfinishtextpreviewfunc) | - | 从TextEditorProxy中获取FinishTextPreviewFunc函数。 |
| [InputMethod\_ErrorCode OH\_TextEditorProxy\_SetCallbackInMainThread(InputMethod\_TextEditorProxy \*proxy, bool isCallbackInMainThread)](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_setcallbackinmainthread) | - | 配置回调函数的执行线程策略。 |

## 函数说明

### OH\_TextEditorProxy\_GetTextConfigFunc()

```c
typedef void (*OH_TextEditorProxy_GetTextConfigFunc)(InputMethod_TextEditorProxy *textEditorProxy, InputMethod_TextConfig *config)
```

**描述**

输入法获取输入框配置时触发的回调函数。开发者需实现此函数，在函数中对config参数设置编辑框的配置信息（输入类型、回车键类型、光标信息等），输入法框架将据此调整键盘布局和输入行为。

使用场景：当输入法应用需要获取编辑框的配置信息时，系统将自动调用此回调。此回调是输入法与编辑器交互的核心回调之一，必须实现。

使用后效果：回调返回后，输入法框架将读取config中的配置信息并据此调整键盘行为。config参数的内存将在回调返回后被释放，不可再访问。

前置条件：须通过[OH\_TextEditorProxy\_SetGetTextConfigFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_setgettextconfigfunc)将此回调设置到TextEditorProxy中，并通过[OH\_InputMethodController\_Attach](capi-inputmethod-controller-capi-h.md#oh_inputmethodcontroller_attach)完成注册。此回调的执行线程由调用Attach的线程决定，不受[OH\_TextEditorProxy\_SetCallbackInMainThread](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_setcallbackinmainthread)影响。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md) \*textEditorProxy | 输入指针，指向当前被回调的[InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md)实例。用于标识触发回调的代理对象。 |
| [InputMethod\_TextConfig](capi-inputmethod-inputmethod-textconfig.md) \*config | 输出指针，表示指向[InputMethod\_TextConfig](capi-inputmethod-inputmethod-textconfig.md)实例的指针。需要在函数实现中对其设置各配置属性（输入类型、回车键类型、光标信息等）以填充输入框配置。此指针仅在回调执行期间有效，回调返回后该内存将被释放，不可再访问。开发者必须在回调内部完成所有设置操作，不得在回调外部继续使用此指针。 |

### OH\_TextEditorProxy\_InsertTextFunc()

```c
typedef void (*OH_TextEditorProxy_InsertTextFunc)(InputMethod_TextEditorProxy *textEditorProxy, const char16_t *text, size_t length)
```

**描述**

输入法应用插入文本时触发的回调函数。开发者需实现此函数，在函数中将text参数指定的文本内容插入到编辑框的光标位置。

使用场景：当输入法应用向编辑框插入文本时（如用户选择候选词、输入字符等），系统将自动调用此回调。此回调是输入法与编辑器交互的核心回调之一，必须实现。

使用后效果：回调执行后，编辑框应在光标位置插入指定文本，并更新文本内容和光标位置。

前置条件：须通过[OH\_TextEditorProxy\_SetInsertTextFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_setinserttextfunc)将此回调设置到TextEditorProxy中，并通过Attach完成注册。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md) \*textEditorProxy | 输入指针，指向当前被回调的TextEditorProxy实例。 |
| const char16\_t \*text | 输入指针，插入的文本内容，采用UTF-16编码。此指针仅在回调执行期间有效，回调返回后该内存将被释放，不可再访问。开发者应在回调内部完成必要的数据拷贝或处理。 |
| size\_t length | 输入参数，插入字符的数量（单位：char16\_t字符个数）。取值范围：大于0。 |

### OH\_TextEditorProxy\_DeleteForwardFunc()

```c
typedef void (*OH_TextEditorProxy_DeleteForwardFunc)(InputMethod_TextEditorProxy *textEditorProxy, int32_t length)
```

**描述**

输入法删除光标右侧文本时触发的回调函数。开发者需实现此函数，在函数中从光标位置向右删除指定数量的字符。

使用场景：当输入法应用请求删除光标右侧文本时（如用户在输入法中执行向前删除操作），系统将自动调用此回调。

使用后效果：回调执行后，编辑框应从光标位置向右删除指定数量的字符，并更新文本内容和光标位置。

前置条件：须通过[OH\_TextEditorProxy\_SetDeleteForwardFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_setdeleteforwardfunc)将此回调设置到TextEditorProxy中，并通过Attach完成注册。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md) \*textEditorProxy | 输入指针，指向当前被回调的TextEditorProxy实例。 |
| int32\_t length | 输入参数，要删除的字符数量（单位：字符个数）。取值范围：大于0。取值原则：若length超过光标右侧剩余文本长度，应删除到文本末尾；否则删除指定数量的字符。 |

### OH\_TextEditorProxy\_DeleteBackwardFunc()

```c
typedef void (*OH_TextEditorProxy_DeleteBackwardFunc)(InputMethod_TextEditorProxy *textEditorProxy, int32_t length)
```

**描述**

输入法删除光标左侧文本时触发的回调函数。开发者需实现此函数，在函数中从光标位置向左删除指定数量的字符。

使用场景：当输入法应用请求删除光标左侧文本时（如用户在输入法中执行退格删除操作），系统将自动调用此回调。

使用后效果：回调执行后，编辑框应从光标位置向左删除指定数量的字符，并更新文本内容和光标位置。

前置条件：须通过[OH\_TextEditorProxy\_SetDeleteBackwardFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_setdeletebackwardfunc)将此回调设置到TextEditorProxy中，并通过Attach完成注册。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md) \*textEditorProxy | 输入指针，指向当前被回调的TextEditorProxy实例。 |
| int32\_t length | 输入参数，要删除的字符数量（单位：字符个数）。取值范围：大于0。取值原则：若length超过光标左侧已有文本长度，应删除到文本开头；否则删除指定数量的字符。 |

### OH\_TextEditorProxy\_SendKeyboardStatusFunc()

```c
typedef void (*OH_TextEditorProxy_SendKeyboardStatusFunc)(InputMethod_TextEditorProxy *textEditorProxy, InputMethod_KeyboardStatus keyboardStatus)
```

**描述**

输入法通知键盘状态时触发的回调函数。开发者需实现此函数，在函数中根据keyboardStatus参数更新编辑框对键盘状态的感知。

使用场景：当输入法应用的键盘状态发生变化（显示或隐藏）时，系统将自动调用此回调，通知编辑框当前的键盘状态。

使用后效果：回调执行后，编辑框应据此更新对键盘可见性的感知，例如调整避让策略或UI布局。

前置条件：须通过[OH\_TextEditorProxy\_SetSendKeyboardStatusFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_setsendkeyboardstatusfunc)将此回调设置到TextEditorProxy中，并通过Attach完成注册。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md) \*textEditorProxy | 输入指针，指向当前被回调的TextEditorProxy实例。 |
| [InputMethod\_KeyboardStatus](capi-inputmethod-types-capi-h.md#inputmethod_keyboardstatus) keyboardStatus | 输入参数，键盘状态。取值范围：[InputMethod\_KeyboardStatus](capi-inputmethod-types-capi-h.md#inputmethod_keyboardstatus)枚举值（IME\_KEYBOARD\_STATUS\_NONE=0、IME\_KEYBOARD\_STATUS\_HIDE=1、IME\_KEYBOARD\_STATUS\_SHOW=2）。使用后效果：设置为IME\_KEYBOARD\_STATUS\_SHOW时表示键盘已弹出，IME\_KEYBOARD\_STATUS\_HIDE时表示键盘已收起。 |

### OH\_TextEditorProxy\_SendEnterKeyFunc()

```c
typedef void (*OH_TextEditorProxy_SendEnterKeyFunc)(InputMethod_TextEditorProxy *textEditorProxy, InputMethod_EnterKeyType enterKeyType)
```

**描述**

输入法发送回车键时触发的回调函数。开发者需实现此函数，在函数中根据enterKeyType参数执行对应的回车键动作。

使用场景：当输入法应用通知编辑框回车键事件时，系统将自动调用此回调。

使用后效果：回调执行后，编辑框应据此执行对应的回车键行为（如搜索、发送、完成等）。

前置条件：须通过[OH\_TextEditorProxy\_SetSendEnterKeyFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_setsendenterkeyfunc)将此回调设置到TextEditorProxy中，并通过Attach完成注册。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md) \*textEditorProxy | 输入指针，指向当前被回调的TextEditorProxy实例。 |
| [InputMethod\_EnterKeyType](capi-inputmethod-types-capi-h.md#inputmethod_enterkeytype) enterKeyType | 输入参数，回车键类型。取值范围：[InputMethod\_EnterKeyType](capi-inputmethod-types-capi-h.md#inputmethod_enterkeytype)枚举值。使用后效果：不同类型对应不同的回车键行为，如IME\_ENTER\_KEY\_GO表示"前往"、IME\_ENTER\_KEY\_SEARCH表示"搜索"等。 |

### OH\_TextEditorProxy\_MoveCursorFunc()

```c
typedef void (*OH_TextEditorProxy_MoveCursorFunc)(InputMethod_TextEditorProxy *textEditorProxy, InputMethod_Direction direction)
```

**描述**

输入法移动光标时触发的回调函数。开发者需实现此函数，在函数中根据direction参数移动编辑框中的光标位置。

使用场景：当输入法应用请求移动光标时，系统将自动调用此回调。

使用后效果：回调执行后，编辑框应据此移动光标位置，并更新光标显示。

前置条件：须通过[OH\_TextEditorProxy\_SetMoveCursorFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_setmovecursorfunc)将此回调设置到TextEditorProxy中，并通过Attach完成注册。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md) \*textEditorProxy | 输入指针，指向当前被回调的TextEditorProxy实例。 |
| [InputMethod\_Direction](capi-inputmethod-types-capi-h.md#inputmethod_direction) direction | 输入参数，光标移动方向。取值范围：[InputMethod\_Direction](capi-inputmethod-types-capi-h.md#inputmethod_direction)枚举值。使用后效果：不同方向对应不同的光标移动行为，如IME\_DIRECTION\_UP表示上移、IME\_DIRECTION\_DOWN表示下移、IME\_DIRECTION\_LEFT表示左移、IME\_DIRECTION\_RIGHT表示右移。 |

### OH\_TextEditorProxy\_HandleSetSelectionFunc()

```c
typedef void (*OH_TextEditorProxy_HandleSetSelectionFunc)(InputMethod_TextEditorProxy *textEditorProxy, int32_t start, int32_t end)
```

**描述**

输入法请求选中文本时触发的回调函数。开发者需实现此函数，在函数中根据start和end参数选中编辑框中的指定范围文本。

使用场景：当输入法应用请求选中编辑框中一段文本时，系统将自动调用此回调。

使用后效果：回调执行后，编辑框应将start到end范围内的文本选中，并更新选中状态和UI显示。

前置条件：须通过[OH\_TextEditorProxy\_SetHandleSetSelectionFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_sethandlesetselectionfunc)将此回调设置到TextEditorProxy中，并通过Attach完成注册。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md) \*textEditorProxy | 输入指针，指向当前被回调的TextEditorProxy实例。 |
| int32\_t start | 输入参数，选中文本的起始位置（单位：字符偏移量，从0开始计数）。取值原则：start应大于等于0且小于等于end。 |
| int32\_t end | 输入参数，选中文本的结束位置（单位：字符偏移量，从0开始计数）。取值原则：end应大于等于start且小于文本总长度。 |

### OH\_TextEditorProxy\_HandleExtendActionFunc()

```c
typedef void (*OH_TextEditorProxy_HandleExtendActionFunc)(InputMethod_TextEditorProxy *textEditorProxy, InputMethod_ExtendAction action)
```

**描述**

输入法发送扩展编辑操作时触发的回调函数。开发者需实现此函数，在函数中根据action参数执行对应的扩展编辑操作。

使用场景：当输入法应用请求执行扩展编辑操作（如剪切、复制、全选等）时，系统将自动调用此回调。

使用后效果：回调执行后，编辑框应据此执行对应的扩展编辑动作。

前置条件：须通过[OH\_TextEditorProxy\_SetHandleExtendActionFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_sethandleextendactionfunc)将此回调设置到TextEditorProxy中，并通过Attach完成注册。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md) \*textEditorProxy | 输入指针，指向当前被回调的TextEditorProxy实例。 |
| [InputMethod\_ExtendAction](capi-inputmethod-types-capi-h.md#inputmethod_extendaction) action | 输入参数，扩展编辑操作。取值范围：[InputMethod\_ExtendAction](capi-inputmethod-types-capi-h.md#inputmethod_extendaction)枚举值。使用后效果：不同操作对应不同的编辑行为，如IME\_EXTEND\_ACTION\_SELECT\_ALL表示全选、IME\_EXTEND\_ACTION\_CUT表示剪切、IME\_EXTEND\_ACTION\_COPY表示复制等。 |

### OH\_TextEditorProxy\_GetLeftTextOfCursorFunc()

```c
typedef void (*OH_TextEditorProxy_GetLeftTextOfCursorFunc)(InputMethod_TextEditorProxy *textEditorProxy, int32_t number, char16_t text[], size_t *length)
```

**描述**

输入法获取光标左侧文本时触发的回调函数。开发者需实现此函数，在函数中将光标左侧指定数量的文本内容写入text参数，并将实际字符数量写入length参数。

使用场景：当输入法应用需要获取光标左侧的文本内容（如用于联想输入、上下文分析等）时，系统将自动调用此回调。

使用后效果：回调返回后，输入法应用将读取text和length中的数据用于上下文分析。

前置条件：须通过[OH\_TextEditorProxy\_SetGetLeftTextOfCursorFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_setgetlefttextofcursorfunc)将此回调设置到TextEditorProxy中，并通过Attach完成注册。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md) \*textEditorProxy | 输入指针，指向当前被回调的TextEditorProxy实例。 |
| int32\_t number | 输入参数，要获取的字符数量（单位：字符个数）。取值范围：大于0。取值原则：若number超过光标左侧已有文本长度，应返回左侧全部文本。 |
| char16\_t text[] | 输出指针，光标左侧指定长度的文本内容，需要在函数实现中对它赋值。采用UTF-16编码。此指针仅在回调执行期间有效，回调返回后该内存将被释放，不可再访问。开发者需在回调内部完成赋值操作。 |
| size\_t \*length | 输出指针，用于返回实际获取到的字符数量（单位：char16\_t字符个数）。由调用者（输入法框架）分配内存，开发者需在回调内部对\*length赋值。 |

### OH\_TextEditorProxy\_GetRightTextOfCursorFunc()

```c
typedef void (*OH_TextEditorProxy_GetRightTextOfCursorFunc)(InputMethod_TextEditorProxy *textEditorProxy, int32_t number, char16_t text[], size_t *length)
```

**描述**

输入法获取光标右侧文本时触发的回调函数。开发者需实现此函数，在函数中将光标右侧指定数量的文本内容写入text参数，并将实际字符数量写入length参数。

使用场景：当输入法应用需要获取光标右侧的文本内容时，系统将自动调用此回调。

使用后效果：回调返回后，输入法应用将读取text和length中的数据用于上下文分析。

前置条件：须通过[OH\_TextEditorProxy\_SetGetRightTextOfCursorFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_setgetrighttextofcursorfunc)将此回调设置到TextEditorProxy中，并通过Attach完成注册。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md) \*textEditorProxy | 输入指针，指向当前被回调的TextEditorProxy实例。 |
| int32\_t number | 输入参数，要获取的字符数量（单位：字符个数）。取值范围：大于0。取值原则：若number超过光标右侧剩余文本长度，应返回右侧全部文本。 |
| char16\_t text[] | 输出指针，光标右侧指定长度的文本内容，需要在函数实现中对它赋值。采用UTF-16编码。此指针仅在回调执行期间有效，回调返回后该内存将被释放，不可再访问。 |
| size\_t \*length | 输出指针，用于返回实际获取到的字符数量（单位：char16\_t字符个数）。由调用者分配内存，开发者需在回调内部对\*length赋值。 |

### OH\_TextEditorProxy\_GetTextIndexAtCursorFunc()

```c
typedef int32_t (*OH_TextEditorProxy_GetTextIndexAtCursorFunc)(InputMethod_TextEditorProxy *textEditorProxy)
```

**描述**

输入法获取光标所在输入框文本索引时触发的回调函数。开发者需实现此函数，在函数中返回光标在编辑框文本中的字符索引位置。

使用场景：当输入法应用需要获取光标在文本中的精确位置时，系统将自动调用此回调。

使用后效果：回调返回后，输入法应用将读取返回的索引值用于定位上下文。

前置条件：须通过[OH\_TextEditorProxy\_SetGetTextIndexAtCursorFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_setgettextindexatcursorfunc)将此回调设置到TextEditorProxy中，并通过Attach完成注册。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md) \*textEditorProxy | 输入指针，指向当前被回调的TextEditorProxy实例。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回光标在文本内容中的字符索引位置，索引从0开始计数（单位：字符偏移量）。取值范围：大于等于0且小于文本总长度。 |

### OH\_TextEditorProxy\_ReceivePrivateCommandFunc()

```c
typedef int32_t (*OH_TextEditorProxy_ReceivePrivateCommandFunc)(InputMethod_TextEditorProxy *textEditorProxy, InputMethod_PrivateCommand *privateCommand[], size_t size)
```

**描述**

输入法应用发送私有数据命令时触发的回调函数。开发者需实现此函数，在函数中处理输入法应用发送的私有命令数据。

使用场景：当输入法应用通过[OH\_InputMethodProxy\_SendPrivateCommand](capi-inputmethod-inputmethod-proxy-capi-h.md#oh_inputmethodproxy_sendprivatecommand)向编辑框发送私有命令时，系统将自动调用此回调。

使用后效果：回调返回后，输入法应用将根据返回值判断命令是否被成功处理。

前置条件：须通过[OH\_TextEditorProxy\_SetReceivePrivateCommandFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_setreceiveprivatecommandfunc)将此回调设置到TextEditorProxy中，并通过Attach完成注册。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md) \*textEditorProxy | 输入指针，指向当前被回调的TextEditorProxy实例。 |
| [InputMethod\_PrivateCommand](capi-inputmethod-inputmethod-privatecommand.md) \*privateCommand[] | 输入指针，私有数据命令数组。此指针仅在回调执行期间有效，回调返回后该内存将被释放，不可再访问。开发者应在回调内部完成必要的数据拷贝或处理，不得在回调外部继续使用此指针。 |
| size\_t size | 输入参数，私有数据命令数组中的元素数量。取值范围：大于0且不超过5。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回对私有数据命令的处理结果。0表示成功，非0表示失败。 |

### OH\_TextEditorProxy\_SetPreviewTextFunc()

```c
typedef int32_t (*OH_TextEditorProxy_SetPreviewTextFunc)(InputMethod_TextEditorProxy *textEditorProxy, const char16_t text[], size_t length, int32_t start, int32_t end)
```

**描述**

输入法设置预上屏文本时触发的回调函数。预上屏是输入法的候选文本展示功能，通常在用户输入拼音或输入码未确定汉字时显示。此函数负责设置预上屏文本及其光标位置。与[OH\_TextEditorProxy\_FinishTextPreviewFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_finishtextpreviewfunc)配合使用：先调用SetPreviewTextFunc设置预上屏内容，当用户选择候选词或取消输入时，调用FinishTextPreviewFunc结束预上屏。

使用场景：当输入法应用需要展示候选文本（如拼音输入时的预上屏文本）时，系统将自动调用此回调。

使用后效果：回调执行后，编辑框应将text内容以预上屏样式显示在start到end范围内，并将返回值反馈给输入法。

前置条件：须通过[OH\_TextEditorProxy\_SetSetPreviewTextFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_setsetpreviewtextfunc)将此回调设置到TextEditorProxy中，并通过Attach完成注册。编辑框需在TextConfig中设置支持预上屏（supported=true）。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md) \*textEditorProxy | 输入指针，指向当前被回调的TextEditorProxy实例。 |
| const char16\_t text[] | 输入指针，请求设置为预上屏样式的文本内容，采用UTF-16编码。此指针仅在回调执行期间有效，回调返回后该内存将被释放，不可再访问。开发者应在回调内部完成必要的数据拷贝。 |
| size\_t length | 输入参数，预上屏文本的字符数量（单位：char16\_t字符个数）。 |
| int32\_t start | 输入参数，预上屏文本起始光标位置（单位：字符偏移量，相对于文本开头）。取值原则：start应大于等于0且小于等于end。 |
| int32\_t end | 输入参数，预上屏文本结束光标位置（单位：字符偏移量，相对于文本开头）。取值原则：end应大于等于start且小于文本总长度。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回处理结果。0表示成功，非0表示失败。 |

### OH\_TextEditorProxy\_FinishTextPreviewFunc()

```c
typedef void (*OH_TextEditorProxy_FinishTextPreviewFunc)(InputMethod_TextEditorProxy *textEditorProxy)
```

**描述**

输入法结束预上屏时触发的回调函数。此函数用于清理预上屏状态，通常在用户选择候选词（确定输入）或取消输入时调用。与[OH\_TextEditorProxy\_SetPreviewTextFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_setpreviewtextfunc)配合使用。

使用场景：当输入法应用需要结束预上屏状态时，系统将自动调用此回调。

使用后效果：回调执行后，编辑框应清理预上屏显示状态，恢复到正常文本显示。

前置条件：须通过[OH\_TextEditorProxy\_SetFinishTextPreviewFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_setfinishtextpreviewfunc)将此回调设置到TextEditorProxy中，并通过Attach完成注册。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md) \*textEditorProxy | 输入指针，指向当前被回调的TextEditorProxy实例。 |

### OH\_TextEditorProxy\_Create()

```c
InputMethod_TextEditorProxy *OH_TextEditorProxy_Create(void)
```

**描述**

创建一个新的[InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md)实例。创建后需通过Set\*Func接口注册回调函数，再通过[OH\_InputMethodController\_Attach](capi-inputmethod-controller-capi-h.md#oh_inputmethodcontroller_attach)完成绑定注册。

使用场景：当应用需要创建文本编辑器代理对象以接收输入法请求和通知时调用此函数。

使用后效果：创建成功后返回一个新的TextEditorProxy实例指针，后续可通过Set\*Func接口注册回调函数。

生命周期管理：返回的对象必须通过[OH\_TextEditorProxy\_Destroy](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_destroy)销毁，Create与Destroy必须配对使用。未销毁会导致内存泄漏。同一个实例只能被销毁一次。

**起始版本：** 12

**返回：**

| 类型 | 说明 |
| --- | --- |
| [InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md) \* | 如果创建成功，返回一个指向新创建的[InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md)实例的指针。如果创建失败，返回NULL，可能的失败原因有内存不足。返回NULL时应检查系统内存状态。返回的指针在使用完毕后必须通过[OH\_TextEditorProxy\_Destroy](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_destroy)销毁，销毁后指针应设置为NULL避免误用。 |

### OH\_TextEditorProxy\_Destroy()

```c
void OH_TextEditorProxy_Destroy(InputMethod_TextEditorProxy *proxy)
```

**描述**

销毁一个[InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md)实例。销毁后proxy指针不可再使用，建议将指针设置为NULL避免误用。

使用场景：当应用不再需要TextEditorProxy对象时（如Detach后或应用退出时）调用此函数释放资源。

使用后效果：proxy对象将被释放，其内部资源被回收，此后不可再通过proxy指针调用任何函数。

生命周期管理：与[OH\_TextEditorProxy\_Create](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_create)配对使用，Create返回的对象必须最终通过Destroy释放。同一个实例只能被销毁一次，不可重复销毁。若proxy为NULL，函数不做任何处理。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md) \*proxy | 输入指针，表示指向即将被销毁的[InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md)实例的指针。若传入NULL，函数不做任何处理，不会导致崩溃。销毁后该指针失效，建议设置为NULL。 |

### OH\_TextEditorProxy\_SetGetTextConfigFunc()

```c
InputMethod_ErrorCode OH_TextEditorProxy_SetGetTextConfigFunc(InputMethod_TextEditorProxy *proxy, OH_TextEditorProxy_GetTextConfigFunc getTextConfigFunc)
```

**描述**

将函数[OH\_TextEditorProxy\_GetTextConfigFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_gettextconfigfunc)设置到[InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md)中。此设置须在Attach之前完成，Attach后设置的回调不会被输入法调用。

使用场景：当应用需要注册GetTextConfigFunc回调以响应输入法获取配置请求时调用此函数。

使用后效果：设置成功后，GetTextConfigFunc回调将被注册到TextEditorProxy中，Attach后当输入法请求获取配置时将自动触发此回调。

前置条件：proxy须先通过[OH\_TextEditorProxy\_Create](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_create)创建。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md) \*proxy | 输入指针，指向即将被设置的[InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md)实例的指针。不可为NULL，若传入NULL将返回IME\_ERR\_NULL\_POINTER。 |
| [OH\_TextEditorProxy\_GetTextConfigFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_gettextconfigfunc) getTextConfigFunc | 输入参数，表示被设置到proxy的回调函数[OH\_TextEditorProxy\_GetTextConfigFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_gettextconfigfunc)。不可为NULL。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [InputMethod\_ErrorCode](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) | 返回一个特定的错误码。  [IME\_ERR\_OK](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 表示成功。  [IME\_ERR\_NULL\_POINTER](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 非预期的空指针，proxy或getTextConfigFunc为NULL。  具体错误码可以参考[InputMethod\_ErrorCode](capi-inputmethod-types-capi-h.md#inputmethod_errorcode)。 |

### OH\_TextEditorProxy\_SetInsertTextFunc()

```c
InputMethod_ErrorCode OH_TextEditorProxy_SetInsertTextFunc(InputMethod_TextEditorProxy *proxy, OH_TextEditorProxy_InsertTextFunc insertTextFunc)
```

**描述**

将函数[OH\_TextEditorProxy\_InsertTextFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_inserttextfunc)设置到[InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md)中。此设置须在Attach之前完成。

使用场景：当应用需要注册InsertTextFunc回调以响应输入法插入文本请求时调用此函数。

使用后效果：设置成功后，InsertTextFunc回调将被注册到TextEditorProxy中，Attach后当输入法请求插入文本时将自动触发此回调。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md) \*proxy | 输入指针，指向即将被设置的TextEditorProxy实例的指针。不可为NULL。 |
| [OH\_TextEditorProxy\_InsertTextFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_inserttextfunc) insertTextFunc | 输入参数，表示被设置到proxy的回调函数。不可为NULL。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [InputMethod\_ErrorCode](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) | 返回一个特定的错误码。  [IME\_ERR\_OK](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 表示成功。  [IME\_ERR\_NULL\_POINTER](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 非预期的空指针。  具体错误码可以参考[InputMethod\_ErrorCode](capi-inputmethod-types-capi-h.md#inputmethod_errorcode)。 |

### OH\_TextEditorProxy\_SetDeleteForwardFunc()

```c
InputMethod_ErrorCode OH_TextEditorProxy_SetDeleteForwardFunc(InputMethod_TextEditorProxy *proxy, OH_TextEditorProxy_DeleteForwardFunc deleteForwardFunc)
```

**描述**

将函数[OH\_TextEditorProxy\_DeleteForwardFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_deleteforwardfunc)设置到[InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md)中。此设置须在Attach之前完成。

使用场景：当应用需要注册DeleteForwardFunc回调以响应输入法删除光标右侧文本请求时调用此函数。

使用后效果：设置成功后，DeleteForwardFunc回调将被注册到TextEditorProxy中，Attach后当输入法请求删除光标右侧文本时将自动触发此回调。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md) \*proxy | 输入指针，指向即将被设置的TextEditorProxy实例的指针。不可为NULL。 |
| [OH\_TextEditorProxy\_DeleteForwardFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_deleteforwardfunc) deleteForwardFunc | 输入参数，表示被设置到proxy的回调函数。不可为NULL。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [InputMethod\_ErrorCode](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) | 返回一个特定的错误码。  [IME\_ERR\_OK](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 表示成功。  [IME\_ERR\_NULL\_POINTER](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 非预期的空指针。  具体错误码可以参考[InputMethod\_ErrorCode](capi-inputmethod-types-capi-h.md#inputmethod_errorcode)。 |

### OH\_TextEditorProxy\_SetDeleteBackwardFunc()

```c
InputMethod_ErrorCode OH_TextEditorProxy_SetDeleteBackwardFunc(InputMethod_TextEditorProxy *proxy, OH_TextEditorProxy_DeleteBackwardFunc deleteBackwardFunc)
```

**描述**

将函数[OH\_TextEditorProxy\_DeleteBackwardFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_deletebackwardfunc)设置到[InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md)中。此设置须在Attach之前完成。

使用场景：当应用需要注册DeleteBackwardFunc回调以响应输入法删除光标左侧文本请求时调用此函数。

使用后效果：设置成功后，DeleteBackwardFunc回调将被注册到TextEditorProxy中，Attach后当输入法请求删除光标左侧文本时将自动触发此回调。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md) \*proxy | 输入指针，指向即将被设置的TextEditorProxy实例的指针。不可为NULL。 |
| [OH\_TextEditorProxy\_DeleteBackwardFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_deletebackwardfunc) deleteBackwardFunc | 输入参数，表示被设置到proxy的回调函数。不可为NULL。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [InputMethod\_ErrorCode](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) | 返回一个特定的错误码。  [IME\_ERR\_OK](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 表示成功。  [IME\_ERR\_NULL\_POINTER](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 非预期的空指针。  具体错误码可以参考[InputMethod\_ErrorCode](capi-inputmethod-types-capi-h.md#inputmethod_errorcode)。 |

### OH\_TextEditorProxy\_SetSendKeyboardStatusFunc()

```c
InputMethod_ErrorCode OH_TextEditorProxy_SetSendKeyboardStatusFunc(InputMethod_TextEditorProxy *proxy, OH_TextEditorProxy_SendKeyboardStatusFunc sendKeyboardStatusFunc)
```

**描述**

将函数[OH\_TextEditorProxy\_SendKeyboardStatusFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_sendkeyboardstatusfunc)设置到[InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md)中。此设置须在Attach之前完成。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md) \*proxy | 输入指针，指向即将被设置的TextEditorProxy实例的指针。不可为NULL。 |
| [OH\_TextEditorProxy\_SendKeyboardStatusFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_sendkeyboardstatusfunc) sendKeyboardStatusFunc | 输入参数，表示被设置到proxy的回调函数。不可为NULL。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [InputMethod\_ErrorCode](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) | 返回一个特定的错误码。  [IME\_ERR\_OK](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 表示成功。  [IME\_ERR\_NULL\_POINTER](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 非预期的空指针。  具体错误码可以参考[InputMethod\_ErrorCode](capi-inputmethod-types-capi-h.md#inputmethod_errorcode)。 |

### OH\_TextEditorProxy\_SetSendEnterKeyFunc()

```c
InputMethod_ErrorCode OH_TextEditorProxy_SetSendEnterKeyFunc(InputMethod_TextEditorProxy *proxy, OH_TextEditorProxy_SendEnterKeyFunc sendEnterKeyFunc)
```

**描述**

将函数[OH\_TextEditorProxy\_SendEnterKeyFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_sendenterkeyfunc)设置到[InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md)中。此设置须在Attach之前完成。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md) \*proxy | 输入指针，指向即将被设置的TextEditorProxy实例的指针。不可为NULL。 |
| [OH\_TextEditorProxy\_SendEnterKeyFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_sendenterkeyfunc) sendEnterKeyFunc | 输入参数，表示被设置到proxy的回调函数。不可为NULL。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [InputMethod\_ErrorCode](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) | 返回一个特定的错误码。  [IME\_ERR\_OK](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 表示成功。  [IME\_ERR\_NULL\_POINTER](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 非预期的空指针。  具体错误码可以参考[InputMethod\_ErrorCode](capi-inputmethod-types-capi-h.md#inputmethod_errorcode)。 |

### OH\_TextEditorProxy\_SetMoveCursorFunc()

```c
InputMethod_ErrorCode OH_TextEditorProxy_SetMoveCursorFunc(InputMethod_TextEditorProxy *proxy, OH_TextEditorProxy_MoveCursorFunc moveCursorFunc)
```

**描述**

将函数[OH\_TextEditorProxy\_MoveCursorFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_movecursorfunc)设置到[InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md)中。此设置须在Attach之前完成。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md) \*proxy | 输入指针，指向即将被设置的TextEditorProxy实例的指针。不可为NULL。 |
| [OH\_TextEditorProxy\_MoveCursorFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_movecursorfunc) moveCursorFunc | 输入参数，表示被设置到proxy的回调函数。不可为NULL。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [InputMethod\_ErrorCode](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) | 返回一个特定的错误码。  [IME\_ERR\_OK](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 表示成功。  [IME\_ERR\_NULL\_POINTER](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 非预期的空指针。  具体错误码可以参考[InputMethod\_ErrorCode](capi-inputmethod-types-capi-h.md#inputmethod_errorcode)。 |

### OH\_TextEditorProxy\_SetHandleSetSelectionFunc()

```c
InputMethod_ErrorCode OH_TextEditorProxy_SetHandleSetSelectionFunc(InputMethod_TextEditorProxy *proxy, OH_TextEditorProxy_HandleSetSelectionFunc handleSetSelectionFunc)
```

**描述**

将函数[OH\_TextEditorProxy\_HandleSetSelectionFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_handlesetselectionfunc)设置到[InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md)中。此设置须在Attach之前完成。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md) \*proxy | 输入指针，指向即将被设置的TextEditorProxy实例的指针。不可为NULL。 |
| [OH\_TextEditorProxy\_HandleSetSelectionFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_handlesetselectionfunc) handleSetSelectionFunc | 输入参数，表示被设置到proxy的回调函数。不可为NULL。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [InputMethod\_ErrorCode](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) | 返回一个特定的错误码。  [IME\_ERR\_OK](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 表示成功。  [IME\_ERR\_NULL\_POINTER](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 非预期的空指针。  具体错误码可以参考[InputMethod\_ErrorCode](capi-inputmethod-types-capi-h.md#inputmethod_errorcode)。 |

### OH\_TextEditorProxy\_SetHandleExtendActionFunc()

```c
InputMethod_ErrorCode OH_TextEditorProxy_SetHandleExtendActionFunc(InputMethod_TextEditorProxy *proxy, OH_TextEditorProxy_HandleExtendActionFunc handleExtendActionFunc)
```

**描述**

将函数[OH\_TextEditorProxy\_HandleExtendActionFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_handleextendactionfunc)设置到[InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md)中。此设置须在Attach之前完成。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md) \*proxy | 输入指针，指向即将被设置的TextEditorProxy实例的指针。不可为NULL。 |
| [OH\_TextEditorProxy\_HandleExtendActionFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_handleextendactionfunc) handleExtendActionFunc | 输入参数，表示被设置到proxy的回调函数。不可为NULL。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [InputMethod\_ErrorCode](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) | 返回一个特定的错误码。  [IME\_ERR\_OK](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 表示成功。  [IME\_ERR\_NULL\_POINTER](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 非预期的空指针。  具体错误码可以参考[InputMethod\_ErrorCode](capi-inputmethod-types-capi-h.md#inputmethod_errorcode)。 |

### OH\_TextEditorProxy\_SetGetLeftTextOfCursorFunc()

```c
InputMethod_ErrorCode OH_TextEditorProxy_SetGetLeftTextOfCursorFunc(InputMethod_TextEditorProxy *proxy, OH_TextEditorProxy_GetLeftTextOfCursorFunc getLeftTextOfCursorFunc)
```

**描述**

将函数[OH\_TextEditorProxy\_GetLeftTextOfCursorFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_getlefttextofcursorfunc)设置到[InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md)中。此设置须在Attach之前完成。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md) \*proxy | 输入指针，指向即将被设置的TextEditorProxy实例的指针。不可为NULL。 |
| [OH\_TextEditorProxy\_GetLeftTextOfCursorFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_getlefttextofcursorfunc) getLeftTextOfCursorFunc | 输入参数，表示被设置到proxy的回调函数。不可为NULL。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [InputMethod\_ErrorCode](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) | 返回一个特定的错误码。  [IME\_ERR\_OK](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 表示成功。  [IME\_ERR\_NULL\_POINTER](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 非预期的空指针。  具体错误码可以参考[InputMethod\_ErrorCode](capi-inputmethod-types-capi-h.md#inputmethod_errorcode)。 |

### OH\_TextEditorProxy\_SetGetRightTextOfCursorFunc()

```c
InputMethod_ErrorCode OH_TextEditorProxy_SetGetRightTextOfCursorFunc(InputMethod_TextEditorProxy *proxy, OH_TextEditorProxy_GetRightTextOfCursorFunc getRightTextOfCursorFunc)
```

**描述**

将函数[OH\_TextEditorProxy\_GetRightTextOfCursorFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_getrighttextofcursorfunc)设置到[InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md)中。此设置须在Attach之前完成。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md) \*proxy | 输入指针，指向即将被设置的TextEditorProxy实例的指针。不可为NULL。 |
| [OH\_TextEditorProxy\_GetRightTextOfCursorFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_getrighttextofcursorfunc) getRightTextOfCursorFunc | 输入参数，表示被设置到proxy的回调函数。不可为NULL。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [InputMethod\_ErrorCode](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) | 返回一个特定的错误码。  [IME\_ERR\_OK](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 表示成功。  [IME\_ERR\_NULL\_POINTER](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 非预期的空指针。  具体错误码可以参考[InputMethod\_ErrorCode](capi-inputmethod-types-capi-h.md#inputmethod_errorcode)。 |

### OH\_TextEditorProxy\_SetGetTextIndexAtCursorFunc()

```c
InputMethod_ErrorCode OH_TextEditorProxy_SetGetTextIndexAtCursorFunc(InputMethod_TextEditorProxy *proxy, OH_TextEditorProxy_GetTextIndexAtCursorFunc getTextIndexAtCursorFunc)
```

**描述**

将函数[OH\_TextEditorProxy\_GetTextIndexAtCursorFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_gettextindexatcursorfunc)设置到[InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md)中。此设置须在Attach之前完成。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md) \*proxy | 输入指针，指向即将被设置的TextEditorProxy实例的指针。不可为NULL。 |
| [OH\_TextEditorProxy\_GetTextIndexAtCursorFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_gettextindexatcursorfunc) getTextIndexAtCursorFunc | 输入参数，表示被设置到proxy的回调函数。不可为NULL。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [InputMethod\_ErrorCode](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) | 返回一个特定的错误码。  [IME\_ERR\_OK](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 表示成功。  [IME\_ERR\_NULL\_POINTER](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 非预期的空指针。  具体错误码可以参考[InputMethod\_ErrorCode](capi-inputmethod-types-capi-h.md#inputmethod_errorcode)。 |

### OH\_TextEditorProxy\_SetReceivePrivateCommandFunc()

```c
InputMethod_ErrorCode OH_TextEditorProxy_SetReceivePrivateCommandFunc(InputMethod_TextEditorProxy *proxy, OH_TextEditorProxy_ReceivePrivateCommandFunc receivePrivateCommandFunc)
```

**描述**

将函数[OH\_TextEditorProxy\_ReceivePrivateCommandFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_receiveprivatecommandfunc)设置到[InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md)中。此设置须在Attach之前完成。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md) \*proxy | 输入指针，指向即将被设置的TextEditorProxy实例的指针。不可为NULL。 |
| [OH\_TextEditorProxy\_ReceivePrivateCommandFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_receiveprivatecommandfunc) receivePrivateCommandFunc | 输入参数，表示被设置到proxy的回调函数。不可为NULL。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [InputMethod\_ErrorCode](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) | 返回一个特定的错误码。  [IME\_ERR\_OK](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 表示成功。  [IME\_ERR\_NULL\_POINTER](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 非预期的空指针。  具体错误码可以参考[InputMethod\_ErrorCode](capi-inputmethod-types-capi-h.md#inputmethod_errorcode)。 |

### OH\_TextEditorProxy\_SetSetPreviewTextFunc()

```c
InputMethod_ErrorCode OH_TextEditorProxy_SetSetPreviewTextFunc(InputMethod_TextEditorProxy *proxy, OH_TextEditorProxy_SetPreviewTextFunc setPreviewTextFunc)
```

**描述**

将函数[OH\_TextEditorProxy\_SetPreviewTextFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_setpreviewtextfunc)设置到[InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md)中。此设置须在Attach之前完成。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md) \*proxy | 输入指针，指向即将被设置的TextEditorProxy实例的指针。不可为NULL。 |
| [OH\_TextEditorProxy\_SetPreviewTextFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_setpreviewtextfunc) setPreviewTextFunc | 输入参数，表示被设置到proxy的回调函数。不可为NULL。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [InputMethod\_ErrorCode](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) | 返回一个特定的错误码。  [IME\_ERR\_OK](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 表示成功。  [IME\_ERR\_NULL\_POINTER](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 非预期的空指针。  具体错误码可以参考[InputMethod\_ErrorCode](capi-inputmethod-types-capi-h.md#inputmethod_errorcode)。 |

### OH\_TextEditorProxy\_SetFinishTextPreviewFunc()

```c
InputMethod_ErrorCode OH_TextEditorProxy_SetFinishTextPreviewFunc(InputMethod_TextEditorProxy *proxy, OH_TextEditorProxy_FinishTextPreviewFunc finishTextPreviewFunc)
```

**描述**

将函数[OH\_TextEditorProxy\_FinishTextPreviewFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_finishtextpreviewfunc)设置到[InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md)中。此设置须在Attach之前完成。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md) \*proxy | 输入指针，指向即将被设置的TextEditorProxy实例的指针。不可为NULL。 |
| [OH\_TextEditorProxy\_FinishTextPreviewFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_finishtextpreviewfunc) finishTextPreviewFunc | 输入参数，表示被设置到proxy的回调函数。不可为NULL。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [InputMethod\_ErrorCode](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) | 返回一个特定的错误码。  [IME\_ERR\_OK](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 表示成功。  [IME\_ERR\_NULL\_POINTER](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 非预期的空指针。  具体错误码可以参考[InputMethod\_ErrorCode](capi-inputmethod-types-capi-h.md#inputmethod_errorcode)。 |

### OH\_TextEditorProxy\_GetGetTextConfigFunc()

```c
InputMethod_ErrorCode OH_TextEditorProxy_GetGetTextConfigFunc(InputMethod_TextEditorProxy *proxy, OH_TextEditorProxy_GetTextConfigFunc *getTextConfigFunc)
```

**描述**

从[InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md)中获取[OH\_TextEditorProxy\_GetTextConfigFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_gettextconfigfunc)函数。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md) \*proxy | 输入指针，指向被读取的TextEditorProxy实例的指针。不可为NULL。 |
| [OH\_TextEditorProxy\_GetTextConfigFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_gettextconfigfunc) \*getTextConfigFunc | 输出指针，表示从proxy获取到的函数指针。由调用者分配内存。不可为NULL。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [InputMethod\_ErrorCode](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) | 返回一个特定的错误码。  [IME\_ERR\_OK](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 表示成功。  [IME\_ERR\_NULL\_POINTER](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 非预期的空指针，proxy或getTextConfigFunc为NULL。  具体错误码可以参考[InputMethod\_ErrorCode](capi-inputmethod-types-capi-h.md#inputmethod_errorcode)。 |

### OH\_TextEditorProxy\_GetInsertTextFunc()

```c
InputMethod_ErrorCode OH_TextEditorProxy_GetInsertTextFunc(InputMethod_TextEditorProxy *proxy, OH_TextEditorProxy_InsertTextFunc *insertTextFunc)
```

**描述**

从[InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md)中获取[OH\_TextEditorProxy\_InsertTextFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_inserttextfunc)函数。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md) \*proxy | 输入指针，指向被读取的TextEditorProxy实例的指针。不可为NULL。 |
| [OH\_TextEditorProxy\_InsertTextFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_inserttextfunc) \*insertTextFunc | 输出指针，表示从proxy获取到的函数指针。由调用者分配内存。不可为NULL。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [InputMethod\_ErrorCode](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) | 返回一个特定的错误码。  [IME\_ERR\_OK](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 表示成功。  [IME\_ERR\_NULL\_POINTER](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 非预期的空指针。  具体错误码可以参考[InputMethod\_ErrorCode](capi-inputmethod-types-capi-h.md#inputmethod_errorcode)。 |

### OH\_TextEditorProxy\_GetDeleteForwardFunc()

```c
InputMethod_ErrorCode OH_TextEditorProxy_GetDeleteForwardFunc(InputMethod_TextEditorProxy *proxy, OH_TextEditorProxy_DeleteForwardFunc *deleteForwardFunc)
```

**描述**

从[InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md)中获取[OH\_TextEditorProxy\_DeleteForwardFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_deleteforwardfunc)函数。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md) \*proxy | 输入指针，指向被读取的TextEditorProxy实例的指针。不可为NULL。 |
| [OH\_TextEditorProxy\_DeleteForwardFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_deleteforwardfunc) \*deleteForwardFunc | 输出指针，表示从proxy获取到的函数指针。不可为NULL。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [InputMethod\_ErrorCode](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) | 返回一个特定的错误码。  [IME\_ERR\_OK](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 表示成功。  [IME\_ERR\_NULL\_POINTER](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 非预期的空指针。  具体错误码可以参考[InputMethod\_ErrorCode](capi-inputmethod-types-capi-h.md#inputmethod_errorcode)。 |

### OH\_TextEditorProxy\_GetDeleteBackwardFunc()

```c
InputMethod_ErrorCode OH_TextEditorProxy_GetDeleteBackwardFunc(InputMethod_TextEditorProxy *proxy, OH_TextEditorProxy_DeleteBackwardFunc *deleteBackwardFunc)
```

**描述**

从[InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md)中获取[OH\_TextEditorProxy\_DeleteBackwardFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_deletebackwardfunc)函数。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md) \*proxy | 输入指针，指向被读取的TextEditorProxy实例的指针。不可为NULL。 |
| [OH\_TextEditorProxy\_DeleteBackwardFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_deletebackwardfunc) \*deleteBackwardFunc | 输出指针，表示从proxy获取到的函数指针。不可为NULL。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [InputMethod\_ErrorCode](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) | 返回一个特定的错误码。  [IME\_ERR\_OK](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 表示成功。  [IME\_ERR\_NULL\_POINTER](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 非预期的空指针。  具体错误码可以参考[InputMethod\_ErrorCode](capi-inputmethod-types-capi-h.md#inputmethod_errorcode)。 |

### OH\_TextEditorProxy\_GetSendKeyboardStatusFunc()

```c
InputMethod_ErrorCode OH_TextEditorProxy_GetSendKeyboardStatusFunc(InputMethod_TextEditorProxy *proxy, OH_TextEditorProxy_SendKeyboardStatusFunc *sendKeyboardStatusFunc)
```

**描述**

从[InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md)中获取[OH\_TextEditorProxy\_SendKeyboardStatusFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_sendkeyboardstatusfunc)函数。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md) \*proxy | 输入指针，指向被读取的TextEditorProxy实例的指针。不可为NULL。 |
| [OH\_TextEditorProxy\_SendKeyboardStatusFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_sendkeyboardstatusfunc) \*sendKeyboardStatusFunc | 输出指针，表示从proxy获取到的函数指针。不可为NULL。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [InputMethod\_ErrorCode](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) | 返回一个特定的错误码。  [IME\_ERR\_OK](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 表示成功。  [IME\_ERR\_NULL\_POINTER](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 非预期的空指针。  具体错误码可以参考[InputMethod\_ErrorCode](capi-inputmethod-types-capi-h.md#inputmethod_errorcode)。 |

### OH\_TextEditorProxy\_GetSendEnterKeyFunc()

```c
InputMethod_ErrorCode OH_TextEditorProxy_GetSendEnterKeyFunc(InputMethod_TextEditorProxy *proxy, OH_TextEditorProxy_SendEnterKeyFunc *sendEnterKeyFunc)
```

**描述**

从[InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md)中获取[OH\_TextEditorProxy\_SendEnterKeyFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_sendenterkeyfunc)函数。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md) \*proxy | 输入指针，指向被读取的TextEditorProxy实例的指针。不可为NULL。 |
| [OH\_TextEditorProxy\_SendEnterKeyFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_sendenterkeyfunc) \*sendEnterKeyFunc | 输出指针，表示从proxy获取到的函数指针。不可为NULL。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [InputMethod\_ErrorCode](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) | 返回一个特定的错误码。  [IME\_ERR\_OK](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 表示成功。  [IME\_ERR\_NULL\_POINTER](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 非预期的空指针。  具体错误码可以参考[InputMethod\_ErrorCode](capi-inputmethod-types-capi-h.md#inputmethod_errorcode)。 |

### OH\_TextEditorProxy\_GetMoveCursorFunc()

```c
InputMethod_ErrorCode OH_TextEditorProxy_GetMoveCursorFunc(InputMethod_TextEditorProxy *proxy, OH_TextEditorProxy_MoveCursorFunc *moveCursorFunc)
```

**描述**

从[InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md)中获取[OH\_TextEditorProxy\_MoveCursorFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_movecursorfunc)函数。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md) \*proxy | 输入指针，指向被读取的TextEditorProxy实例的指针。不可为NULL。 |
| [OH\_TextEditorProxy\_MoveCursorFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_movecursorfunc) \*moveCursorFunc | 输出指针，表示从proxy获取到的函数指针。不可为NULL。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [InputMethod\_ErrorCode](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) | 返回一个特定的错误码。  [IME\_ERR\_OK](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 表示成功。  [IME\_ERR\_NULL\_POINTER](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 非预期的空指针。  具体错误码可以参考[InputMethod\_ErrorCode](capi-inputmethod-types-capi-h.md#inputmethod_errorcode)。 |

### OH\_TextEditorProxy\_GetHandleSetSelectionFunc()

```c
InputMethod_ErrorCode OH_TextEditorProxy_GetHandleSetSelectionFunc(InputMethod_TextEditorProxy *proxy, OH_TextEditorProxy_HandleSetSelectionFunc *handleSetSelectionFunc)
```

**描述**

从[InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md)中获取[OH\_TextEditorProxy\_HandleSetSelectionFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_handlesetselectionfunc)函数。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md) \*proxy | 输入指针，指向被读取的TextEditorProxy实例的指针。不可为NULL。 |
| [OH\_TextEditorProxy\_HandleSetSelectionFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_handlesetselectionfunc) \*handleSetSelectionFunc | 输出指针，表示从proxy获取到的函数指针。不可为NULL。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [InputMethod\_ErrorCode](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) | 返回一个特定的错误码。  [IME\_ERR\_OK](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 表示成功。  [IME\_ERR\_NULL\_POINTER](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 非预期的空指针。  具体错误码可以参考[InputMethod\_ErrorCode](capi-inputmethod-types-capi-h.md#inputmethod_errorcode)。 |

### OH\_TextEditorProxy\_GetHandleExtendActionFunc()

```c
InputMethod_ErrorCode OH_TextEditorProxy_GetHandleExtendActionFunc(InputMethod_TextEditorProxy *proxy, OH_TextEditorProxy_HandleExtendActionFunc *handleExtendActionFunc)
```

**描述**

从[InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md)中获取[OH\_TextEditorProxy\_HandleExtendActionFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_handleextendactionfunc)函数。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md) \*proxy | 输入指针，指向被读取的TextEditorProxy实例的指针。不可为NULL。 |
| [OH\_TextEditorProxy\_HandleExtendActionFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_handleextendactionfunc) \*handleExtendActionFunc | 输出指针，表示从proxy获取到的函数指针。不可为NULL。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [InputMethod\_ErrorCode](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) | 返回一个特定的错误码。  [IME\_ERR\_OK](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 表示成功。  [IME\_ERR\_NULL\_POINTER](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 非预期的空指针。  具体错误码可以参考[InputMethod\_ErrorCode](capi-inputmethod-types-capi-h.md#inputmethod_errorcode)。 |

### OH\_TextEditorProxy\_GetGetLeftTextOfCursorFunc()

```c
InputMethod_ErrorCode OH_TextEditorProxy_GetGetLeftTextOfCursorFunc(InputMethod_TextEditorProxy *proxy, OH_TextEditorProxy_GetLeftTextOfCursorFunc *getLeftTextOfCursorFunc)
```

**描述**

从[InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md)中获取[OH\_TextEditorProxy\_GetLeftTextOfCursorFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_getlefttextofcursorfunc)函数。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md) \*proxy | 输入指针，指向被读取的TextEditorProxy实例的指针。不可为NULL。 |
| [OH\_TextEditorProxy\_GetLeftTextOfCursorFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_getlefttextofcursorfunc) \*getLeftTextOfCursorFunc | 输出指针，表示从proxy获取到的函数指针。不可为NULL。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [InputMethod\_ErrorCode](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) | 返回一个特定的错误码。  [IME\_ERR\_OK](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 表示成功。  [IME\_ERR\_NULL\_POINTER](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 非预期的空指针。  具体错误码可以参考[InputMethod\_ErrorCode](capi-inputmethod-types-capi-h.md#inputmethod_errorcode)。 |

### OH\_TextEditorProxy\_GetGetRightTextOfCursorFunc()

```c
InputMethod_ErrorCode OH_TextEditorProxy_GetGetRightTextOfCursorFunc(InputMethod_TextEditorProxy *proxy, OH_TextEditorProxy_GetRightTextOfCursorFunc *getRightTextOfCursorFunc)
```

**描述**

从[InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md)中获取[OH\_TextEditorProxy\_GetRightTextOfCursorFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_getrighttextofcursorfunc)函数。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md) \*proxy | 输入指针，指向被读取的TextEditorProxy实例的指针。不可为NULL。 |
| [OH\_TextEditorProxy\_GetRightTextOfCursorFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_getrighttextofcursorfunc) \*getRightTextOfCursorFunc | 输出指针，表示从proxy获取到的函数指针。不可为NULL。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [InputMethod\_ErrorCode](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) | 返回一个特定的错误码。  [IME\_ERR\_OK](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 表示成功。  [IME\_ERR\_NULL\_POINTER](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 非预期的空指针。  具体错误码可以参考[InputMethod\_ErrorCode](capi-inputmethod-types-capi-h.md#inputmethod_errorcode)。 |

### OH\_TextEditorProxy\_GetGetTextIndexAtCursorFunc()

```c
InputMethod_ErrorCode OH_TextEditorProxy_GetGetTextIndexAtCursorFunc(InputMethod_TextEditorProxy *proxy, OH_TextEditorProxy_GetTextIndexAtCursorFunc *getTextIndexAtCursorFunc)
```

**描述**

从[InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md)中获取[OH\_TextEditorProxy\_GetTextIndexAtCursorFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_gettextindexatcursorfunc)函数。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md) \*proxy | 输入指针，指向被读取的TextEditorProxy实例的指针。不可为NULL。 |
| [OH\_TextEditorProxy\_GetTextIndexAtCursorFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_gettextindexatcursorfunc) \*getTextIndexAtCursorFunc | 输出指针，表示从proxy获取到的函数指针。不可为NULL。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [InputMethod\_ErrorCode](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) | 返回一个特定的错误码。  [IME\_ERR\_OK](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 表示成功。  [IME\_ERR\_NULL\_POINTER](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 非预期的空指针。  具体错误码可以参考[InputMethod\_ErrorCode](capi-inputmethod-types-capi-h.md#inputmethod_errorcode)。 |

### OH\_TextEditorProxy\_GetReceivePrivateCommandFunc()

```c
InputMethod_ErrorCode OH_TextEditorProxy_GetReceivePrivateCommandFunc(InputMethod_TextEditorProxy *proxy, OH_TextEditorProxy_ReceivePrivateCommandFunc *receivePrivateCommandFunc)
```

**描述**

从[InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md)中获取[OH\_TextEditorProxy\_ReceivePrivateCommandFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_receiveprivatecommandfunc)函数。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md) \*proxy | 输入指针，指向被读取的TextEditorProxy实例的指针。不可为NULL。 |
| [OH\_TextEditorProxy\_ReceivePrivateCommandFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_receiveprivatecommandfunc) \*receivePrivateCommandFunc | 输出指针，表示从proxy获取到的函数指针。不可为NULL。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [InputMethod\_ErrorCode](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) | 返回一个特定的错误码。  [IME\_ERR\_OK](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 表示成功。  [IME\_ERR\_NULL\_POINTER](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 非预期的空指针。  具体错误码可以参考[InputMethod\_ErrorCode](capi-inputmethod-types-capi-h.md#inputmethod_errorcode)。 |

### OH\_TextEditorProxy\_GetSetPreviewTextFunc()

```c
InputMethod_ErrorCode OH_TextEditorProxy_GetSetPreviewTextFunc(InputMethod_TextEditorProxy *proxy, OH_TextEditorProxy_SetPreviewTextFunc *setPreviewTextFunc)
```

**描述**

从[InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md)中获取[OH\_TextEditorProxy\_SetPreviewTextFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_setpreviewtextfunc)函数。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md) \*proxy | 输入指针，指向被读取的TextEditorProxy实例的指针。不可为NULL。 |
| [OH\_TextEditorProxy\_SetPreviewTextFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_setpreviewtextfunc) \*setPreviewTextFunc | 输出指针，表示从proxy获取到的函数指针。不可为NULL。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [InputMethod\_ErrorCode](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) | 返回一个特定的错误码。  [IME\_ERR\_OK](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 表示成功。  [IME\_ERR\_NULL\_POINTER](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 非预期的空指针。  具体错误码可以参考[InputMethod\_ErrorCode](capi-inputmethod-types-capi-h.md#inputmethod_errorcode)。 |

### OH\_TextEditorProxy\_GetFinishTextPreviewFunc()

```c
InputMethod_ErrorCode OH_TextEditorProxy_GetFinishTextPreviewFunc(InputMethod_TextEditorProxy *proxy, OH_TextEditorProxy_FinishTextPreviewFunc *finishTextPreviewFunc)
```

**描述**

从[InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md)中获取[OH\_TextEditorProxy\_FinishTextPreviewFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_finishtextpreviewfunc)函数。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md) \*proxy | 输入指针，指向被读取的TextEditorProxy实例的指针。不可为NULL。 |
| [OH\_TextEditorProxy\_FinishTextPreviewFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_finishtextpreviewfunc) \*finishTextPreviewFunc | 输出指针，表示从proxy获取到的函数指针。不可为NULL。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [InputMethod\_ErrorCode](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) | 返回一个特定的错误码。  [IME\_ERR\_OK](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 表示成功。  [IME\_ERR\_NULL\_POINTER](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 非预期的空指针。  具体错误码可以参考[InputMethod\_ErrorCode](capi-inputmethod-types-capi-h.md#inputmethod_errorcode)。 |

### OH\_TextEditorProxy\_SetCallbackInMainThread()

```c
InputMethod_ErrorCode OH_TextEditorProxy_SetCallbackInMainThread(InputMethod_TextEditorProxy *proxy, bool isCallbackInMainThread)
```

**描述**

为InputMethod\_TextEditorProxy的回调函数配置执行线程（主线程/IPC线程）。本接口仅控制InputMethod\_TextEditorProxy中除[OH\_TextEditorProxy\_GetTextConfigFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_gettextconfigfunc)之外的所有回调函数。[OH\_TextEditorProxy\_GetTextConfigFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_gettextconfigfunc)的执行线程由调用[OH\_InputMethodController\_Attach](capi-inputmethod-controller-capi-h.md#oh_inputmethodcontroller_attach)的线程决定，不受本接口影响。若需GetTextConfigFunc也在主线程执行，需确保Attach在主线程调用。

使用场景：当应用需要避免多线程并发问题时，可将回调切换到主线程执行；当应用对回调响应速度要求较高时，可保持IPC线程执行。

使用后效果：设置为true后，除GetTextConfigFunc外的所有回调将在主线程执行，避免多线程并发但需注意避免在回调内执行耗时操作；设置为false后，回调在IPC线程执行，响应更快但可能存在并发问题。

前置条件：proxy须先通过[OH\_TextEditorProxy\_Create](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_create)创建。建议在Attach之前调用此接口配置线程策略。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md) \*proxy | 输入指针，指向目标InputMethod\_TextEditorProxy实例的指针。不可为NULL，若传入NULL将返回IME\_ERR\_NULL\_POINTER。 |
| bool isCallbackInMainThread | 输入参数，线程执行策略。取值范围：true或false。取值原则：true-回调函数切换至主线程执行（用于避免多线程并发问题），避免在回调内执行耗时操作防止主线程阻塞；false-回调函数在IPC线程执行（可能存在多线程并发情况），响应速度更快。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [InputMethod\_ErrorCode](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) | 返回一个特定的错误码。  [IME\_ERR\_OK](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 配置成功。  [IME\_ERR\_NULL\_POINTER](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 当proxy为NULL时返回。  具体错误码可以参考[InputMethod\_ErrorCode](capi-inputmethod-types-capi-h.md#inputmethod_errorcode)。 |
