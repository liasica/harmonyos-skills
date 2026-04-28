---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-inputmethod-text-editor-proxy-capi-h
title: inputmethod_text_editor_proxy_capi.h
breadcrumb: API参考 > 应用框架 > IME Kit（输入法开发服务） > C API > 头文件 > inputmethod_text_editor_proxy_capi.h
category: harmonyos-references
scraped_at: 2026-04-28T08:06:12+08:00
doc_updated_at: 2026-04-10
content_hash: sha256:83e066326ca3db09ffd3a9dbf3f459ef44ab9bc4b3d375f2eb2c27a689c914a2
---

## 概述

PhonePC/2in1TabletTVWearable

提供一套方法支持应用开发的自绘输入框获取来自输入法应用的通知和请求。

**引用文件：** <inputmethod/inputmethod\_text\_editor\_proxy\_capi.h>

**库：** libohinputmethod.so

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**起始版本：** 12

**相关模块：** [InputMethod](capi-inputmethod.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 结构体

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md) | InputMethod\_TextEditorProxy | 输入框代理。提供了获取来自输入法应用的通知和请求的方法。当输入法向编辑器发送请求或通知时，这些方法将被调用。 |

### 函数

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [typedef void (\*OH\_TextEditorProxy\_GetTextConfigFunc)(InputMethod\_TextEditorProxy \*textEditorProxy, InputMethod\_TextConfig \*config)](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_gettextconfigfunc) | OH\_TextEditorProxy\_GetTextConfigFunc | 输入法获取输入框配置时触发的函数。您需要实现此函数，通过 [OH\_TextEditorProxy\_SetGetTextConfigFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_setgettextconfigfunc) 将它设置到[InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md)中， 并通过[OH\_InputMethodController\_Attach](capi-inputmethod-controller-capi-h.md#oh_inputmethodcontroller_attach)完成注册。 |
| [typedef void (\*OH\_TextEditorProxy\_InsertTextFunc)(InputMethod\_TextEditorProxy \*textEditorProxy, const char16\_t \*text, size\_t length)](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_inserttextfunc) | OH\_TextEditorProxy\_InsertTextFunc | 输入法应用插入文本时触发的函数。您需要实现此函数，通过 [OH\_TextEditorProxy\_SetInsertTextFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_setinserttextfunc) 将它设置到[InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md)中， 并通过[OH\_InputMethodController\_Attach](capi-inputmethod-controller-capi-h.md#oh_inputmethodcontroller_attach)完成注册。 |
| [typedef void (\*OH\_TextEditorProxy\_DeleteForwardFunc)(InputMethod\_TextEditorProxy \*textEditorProxy, int32\_t length)](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_deleteforwardfunc) | OH\_TextEditorProxy\_DeleteForwardFunc | 输入法删除光标右侧文本时触发的函数。您需要实现此函数，通过 [OH\_TextEditorProxy\_SetDeleteForwardFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_setdeleteforwardfunc) 将它设置到[InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md)中， 并通过[OH\_InputMethodController\_Attach](capi-inputmethod-controller-capi-h.md#oh_inputmethodcontroller_attach)完成注册。 |
| [typedef void (\*OH\_TextEditorProxy\_DeleteBackwardFunc)(InputMethod\_TextEditorProxy \*textEditorProxy, int32\_t length)](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_deletebackwardfunc) | OH\_TextEditorProxy\_DeleteBackwardFunc | 输入法删除光标左侧文本时触发的函数。您需要实现此函数，通过 [OH\_TextEditorProxy\_SetDeleteBackwardFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_setdeletebackwardfunc) 将它设置到[InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md)中， 并通过[OH\_InputMethodController\_Attach](capi-inputmethod-controller-capi-h.md#oh_inputmethodcontroller_attach)完成注册。 |
| [typedef void (\*OH\_TextEditorProxy\_SendKeyboardStatusFunc)(InputMethod\_TextEditorProxy \*textEditorProxy, InputMethod\_KeyboardStatus keyboardStatus)](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_sendkeyboardstatusfunc) | OH\_TextEditorProxy\_SendKeyboardStatusFunc | 输入法通知键盘状态时触发的函数。您需要实现此函数，通过 [OH\_TextEditorProxy\_SetSendKeyboardStatusFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_setsendkeyboardstatusfunc) 将它设置到[InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md)中， 并通过[OH\_InputMethodController\_Attach](capi-inputmethod-controller-capi-h.md#oh_inputmethodcontroller_attach)完成注册。 |
| [typedef void (\*OH\_TextEditorProxy\_SendEnterKeyFunc)(InputMethod\_TextEditorProxy \*textEditorProxy, InputMethod\_EnterKeyType enterKeyType)](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_sendenterkeyfunc) | OH\_TextEditorProxy\_SendEnterKeyFunc | 输入法发送回车键时触发的函数。您需要实现此函数，通过 [OH\_TextEditorProxy\_SetSendEnterKeyFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_setsendenterkeyfunc) 将它设置到[InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md)中， 并通过[OH\_InputMethodController\_Attach](capi-inputmethod-controller-capi-h.md#oh_inputmethodcontroller_attach)完成注册。 |
| [typedef void (\*OH\_TextEditorProxy\_MoveCursorFunc)(InputMethod\_TextEditorProxy \*textEditorProxy, InputMethod\_Direction direction)](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_movecursorfunc) | OH\_TextEditorProxy\_MoveCursorFunc | 输入法移动光标时触发的函数。您需要实现此函数，通过 [OH\_TextEditorProxy\_SetMoveCursorFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_setmovecursorfunc) 将它设置到[InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md)中， 并通过[OH\_InputMethodController\_Attach](capi-inputmethod-controller-capi-h.md#oh_inputmethodcontroller_attach)完成注册。 |
| [typedef void (\*OH\_TextEditorProxy\_HandleSetSelectionFunc)(InputMethod\_TextEditorProxy \*textEditorProxy, int32\_t start, int32\_t end)](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_handlesetselectionfunc) | OH\_TextEditorProxy\_HandleSetSelectionFunc | 输入法请求选中文本时触发的函数。您需要实现此函数，通过 [OH\_TextEditorProxy\_SetHandleSetSelectionFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_sethandlesetselectionfunc) 将它设置到[InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md)中， 并通过[OH\_InputMethodController\_Attach](capi-inputmethod-controller-capi-h.md#oh_inputmethodcontroller_attach)完成注册。 |
| [typedef void (\*OH\_TextEditorProxy\_HandleExtendActionFunc)(InputMethod\_TextEditorProxy \*textEditorProxy, InputMethod\_ExtendAction action)](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_handleextendactionfunc) | OH\_TextEditorProxy\_HandleExtendActionFunc | 输入法发送扩展编辑操作时触发的函数。您需要实现此函数，通过 [OH\_TextEditorProxy\_SetHandleExtendActionFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_sethandleextendactionfunc) 将它设置到[InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md)中， 并通过[OH\_InputMethodController\_Attach](capi-inputmethod-controller-capi-h.md#oh_inputmethodcontroller_attach)完成注册。 |
| [typedef void (\*OH\_TextEditorProxy\_GetLeftTextOfCursorFunc)(InputMethod\_TextEditorProxy \*textEditorProxy, int32\_t number, char16\_t text[], size\_t \*length)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-inputmethod-text-editor-proxy-capi-h#oh_texteditorproxy_getlefttextofcursorfunc) | OH\_TextEditorProxy\_GetLeftTextOfCursorFunc | 输入法获取光标左侧文本时触发的函数。您需要实现此函数，通过 [OH\_TextEditorProxy\_SetGetLeftTextOfCursorFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_setgetlefttextofcursorfunc) 将它设置到[InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md)中， 并通过[OH\_InputMethodController\_Attach](capi-inputmethod-controller-capi-h.md#oh_inputmethodcontroller_attach)完成注册。 |
| [typedef void (\*OH\_TextEditorProxy\_GetRightTextOfCursorFunc)(InputMethod\_TextEditorProxy \*textEditorProxy, int32\_t number, char16\_t text[], size\_t \*length)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-inputmethod-text-editor-proxy-capi-h#oh_texteditorproxy_getrighttextofcursorfunc) | OH\_TextEditorProxy\_GetRightTextOfCursorFunc | 输入法获取光标右侧文本时触发的函数。您需要实现此函数，通过 [OH\_TextEditorProxy\_SetGetRightTextOfCursorFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_setgetrighttextofcursorfunc) 将它设置到[InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md)中， 并通过[OH\_InputMethodController\_Attach](capi-inputmethod-controller-capi-h.md#oh_inputmethodcontroller_attach)完成注册。 |
| [typedef int32\_t (\*OH\_TextEditorProxy\_GetTextIndexAtCursorFunc)(InputMethod\_TextEditorProxy \*textEditorProxy)](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_gettextindexatcursorfunc) | OH\_TextEditorProxy\_GetTextIndexAtCursorFunc | 输入法获取光标所在输入框文本索引时触发的函数。您需要实现此函数，通过 [OH\_TextEditorProxy\_SetGetTextIndexAtCursorFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_setgettextindexatcursorfunc) 将它设置到[InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md)中， 并通过[OH\_InputMethodController\_Attach](capi-inputmethod-controller-capi-h.md#oh_inputmethodcontroller_attach)完成注册。 |
| [typedef int32\_t (\*OH\_TextEditorProxy\_ReceivePrivateCommandFunc)(InputMethod\_TextEditorProxy \*textEditorProxy, InputMethod\_PrivateCommand \*privateCommand[], size\_t size)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-inputmethod-text-editor-proxy-capi-h#oh_texteditorproxy_receiveprivatecommandfunc) | OH\_TextEditorProxy\_ReceivePrivateCommandFunc | 输入法应用发送私有数据命令时触发的函数。您需要实现此函数，通过 [OH\_TextEditorProxy\_SetReceivePrivateCommandFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_setreceiveprivatecommandfunc) 将它设置到[InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md)中， 并通过[OH\_InputMethodController\_Attach](capi-inputmethod-controller-capi-h.md#oh_inputmethodcontroller_attach)完成注册。 |
| [typedef int32\_t (\*OH\_TextEditorProxy\_SetPreviewTextFunc)(InputMethod\_TextEditorProxy \*textEditorProxy, const char16\_t text[], size\_t length, int32\_t start, int32\_t end)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-inputmethod-text-editor-proxy-capi-h#oh_texteditorproxy_setpreviewtextfunc) | OH\_TextEditorProxy\_SetPreviewTextFunc | 输入法设置预上屏文本时触发的函数。您需要实现此函数，通过 [OH\_TextEditorProxy\_SetSetPreviewTextFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_setsetpreviewtextfunc) 将它设置到[InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md)中， 并通过[OH\_InputMethodController\_Attach](capi-inputmethod-controller-capi-h.md#oh_inputmethodcontroller_attach)完成注册。 |
| [typedef void (\*OH\_TextEditorProxy\_FinishTextPreviewFunc)(InputMethod\_TextEditorProxy \*textEditorProxy)](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_finishtextpreviewfunc) | OH\_TextEditorProxy\_FinishTextPreviewFunc | 输入法结束预上屏时触发的函数。您需要实现此函数，通过 [OH\_TextEditorProxy\_SetFinishTextPreviewFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_setfinishtextpreviewfunc) 将它设置到[InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md)中， 并通过[OH\_InputMethodController\_Attach](capi-inputmethod-controller-capi-h.md#oh_inputmethodcontroller_attach)完成注册。 |
| [InputMethod\_TextEditorProxy \*OH\_TextEditorProxy\_Create(void)](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_create) | - | 创建一个新的[InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md)实例。 |
| [void OH\_TextEditorProxy\_Destroy(InputMethod\_TextEditorProxy \*proxy)](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_destroy) | - | 销毁一个[InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md)实例。 |
| [InputMethod\_ErrorCode OH\_TextEditorProxy\_SetGetTextConfigFunc(InputMethod\_TextEditorProxy \*proxy, OH\_TextEditorProxy\_GetTextConfigFunc getTextConfigFunc)](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_setgettextconfigfunc) | - | 将函数[OH\_TextEditorProxy\_GetTextConfigFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_gettextconfigfunc)设置到[InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md)中。 |
| [InputMethod\_ErrorCode OH\_TextEditorProxy\_SetInsertTextFunc(InputMethod\_TextEditorProxy \*proxy, OH\_TextEditorProxy\_InsertTextFunc insertTextFunc)](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_setinserttextfunc) | - | 将函数[OH\_TextEditorProxy\_InsertTextFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_inserttextfunc)设置到[InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md)中。 |
| [InputMethod\_ErrorCode OH\_TextEditorProxy\_SetDeleteForwardFunc(InputMethod\_TextEditorProxy \*proxy, OH\_TextEditorProxy\_DeleteForwardFunc deleteForwardFunc)](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_setdeleteforwardfunc) | - | 将函数[OH\_TextEditorProxy\_DeleteForwardFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_deleteforwardfunc)设置到[InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md)中。 |
| [InputMethod\_ErrorCode OH\_TextEditorProxy\_SetDeleteBackwardFunc(InputMethod\_TextEditorProxy \*proxy, OH\_TextEditorProxy\_DeleteBackwardFunc deleteBackwardFunc)](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_setdeletebackwardfunc) | - | 将函数[OH\_TextEditorProxy\_DeleteBackwardFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_deletebackwardfunc)设置到[InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md)中。 |
| [InputMethod\_ErrorCode OH\_TextEditorProxy\_SetSendKeyboardStatusFunc(InputMethod\_TextEditorProxy \*proxy, OH\_TextEditorProxy\_SendKeyboardStatusFunc sendKeyboardStatusFunc)](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_setsendkeyboardstatusfunc) | - | 将函数[OH\_TextEditorProxy\_SendKeyboardStatusFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_sendkeyboardstatusfunc)设置到[InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md)中。 |
| [InputMethod\_ErrorCode OH\_TextEditorProxy\_SetSendEnterKeyFunc(InputMethod\_TextEditorProxy \*proxy, OH\_TextEditorProxy\_SendEnterKeyFunc sendEnterKeyFunc)](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_setsendenterkeyfunc) | - | 将函数[OH\_TextEditorProxy\_SetSendEnterKeyFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_setsendenterkeyfunc)设置到[InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md)中。 |
| [InputMethod\_ErrorCode OH\_TextEditorProxy\_SetMoveCursorFunc(InputMethod\_TextEditorProxy \*proxy, OH\_TextEditorProxy\_MoveCursorFunc moveCursorFunc)](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_setmovecursorfunc) | - | 将函数[OH\_TextEditorProxy\_SetMoveCursorFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_setmovecursorfunc)设置到[InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md)中。 |
| [InputMethod\_ErrorCode OH\_TextEditorProxy\_SetHandleSetSelectionFunc(InputMethod\_TextEditorProxy \*proxy, OH\_TextEditorProxy\_HandleSetSelectionFunc handleSetSelectionFunc)](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_sethandlesetselectionfunc) | - | 将函数[OH\_TextEditorProxy\_HandleSetSelectionFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_handlesetselectionfunc)设置到[InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md)中。 |
| [InputMethod\_ErrorCode OH\_TextEditorProxy\_SetHandleExtendActionFunc(InputMethod\_TextEditorProxy \*proxy, OH\_TextEditorProxy\_HandleExtendActionFunc handleExtendActionFunc)](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_sethandleextendactionfunc) | - | 将函数[OH\_TextEditorProxy\_HandleExtendActionFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_handleextendactionfunc)设置到[InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md)中。 |
| [InputMethod\_ErrorCode OH\_TextEditorProxy\_SetGetLeftTextOfCursorFunc(InputMethod\_TextEditorProxy \*proxy, OH\_TextEditorProxy\_GetLeftTextOfCursorFunc getLeftTextOfCursorFunc)](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_setgetlefttextofcursorfunc) | - | 将函数[OH\_TextEditorProxy\_GetLeftTextOfCursorFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_getlefttextofcursorfunc)设置到[InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md)中。 |
| [InputMethod\_ErrorCode OH\_TextEditorProxy\_SetGetRightTextOfCursorFunc(InputMethod\_TextEditorProxy \*proxy, OH\_TextEditorProxy\_GetRightTextOfCursorFunc getRightTextOfCursorFunc)](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_setgetrighttextofcursorfunc) | - | 将函数[OH\_TextEditorProxy\_GetRightTextOfCursorFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_getrighttextofcursorfunc)设置到[InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md)中。 |
| [InputMethod\_ErrorCode OH\_TextEditorProxy\_SetGetTextIndexAtCursorFunc(InputMethod\_TextEditorProxy \*proxy, OH\_TextEditorProxy\_GetTextIndexAtCursorFunc getTextIndexAtCursorFunc)](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_setgettextindexatcursorfunc) | - | 将函数[OH\_TextEditorProxy\_GetTextIndexAtCursorFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_gettextindexatcursorfunc)设置到[InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md)中。 |
| [InputMethod\_ErrorCode OH\_TextEditorProxy\_SetReceivePrivateCommandFunc(InputMethod\_TextEditorProxy \*proxy, OH\_TextEditorProxy\_ReceivePrivateCommandFunc receivePrivateCommandFunc)](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_setreceiveprivatecommandfunc) | - | 将函数[OH\_TextEditorProxy\_ReceivePrivateCommandFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_receiveprivatecommandfunc)设置到[InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md)中。 |
| [InputMethod\_ErrorCode OH\_TextEditorProxy\_SetSetPreviewTextFunc(InputMethod\_TextEditorProxy \*proxy, OH\_TextEditorProxy\_SetPreviewTextFunc setPreviewTextFunc)](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_setsetpreviewtextfunc) | - | 将函数[OH\_TextEditorProxy\_SetPreviewTextFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_setpreviewtextfunc)设置到[InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md)中。 |
| [InputMethod\_ErrorCode OH\_TextEditorProxy\_SetFinishTextPreviewFunc(InputMethod\_TextEditorProxy \*proxy, OH\_TextEditorProxy\_FinishTextPreviewFunc finishTextPreviewFunc)](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_setfinishtextpreviewfunc) | - | 将函数[OH\_TextEditorProxy\_FinishTextPreviewFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_finishtextpreviewfunc)设置到[InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md)中。 |
| [InputMethod\_ErrorCode OH\_TextEditorProxy\_GetGetTextConfigFunc(InputMethod\_TextEditorProxy \*proxy, OH\_TextEditorProxy\_GetTextConfigFunc \*getTextConfigFunc)](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_getgettextconfigfunc) | - | 从[InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md)中获取[OH\_TextEditorProxy\_GetTextConfigFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_gettextconfigfunc)函数。 |
| [InputMethod\_ErrorCode OH\_TextEditorProxy\_GetInsertTextFunc(InputMethod\_TextEditorProxy \*proxy, OH\_TextEditorProxy\_InsertTextFunc \*insertTextFunc)](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_getinserttextfunc) | - | 从[InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md)中获取[OH\_TextEditorProxy\_InsertTextFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_inserttextfunc)函数。 |
| [InputMethod\_ErrorCode OH\_TextEditorProxy\_GetDeleteForwardFunc(InputMethod\_TextEditorProxy \*proxy, OH\_TextEditorProxy\_DeleteForwardFunc \*deleteForwardFunc)](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_getdeleteforwardfunc) | - | 从[InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md)中获取[OH\_TextEditorProxy\_DeleteForwardFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_deleteforwardfunc)函数。 |
| [InputMethod\_ErrorCode OH\_TextEditorProxy\_GetDeleteBackwardFunc(InputMethod\_TextEditorProxy \*proxy, OH\_TextEditorProxy\_DeleteBackwardFunc \*deleteBackwardFunc)](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_getdeletebackwardfunc) | - | 从[InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md)中获取[OH\_TextEditorProxy\_DeleteBackwardFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_deletebackwardfunc)函数。 |
| [InputMethod\_ErrorCode OH\_TextEditorProxy\_GetSendKeyboardStatusFunc(InputMethod\_TextEditorProxy \*proxy, OH\_TextEditorProxy\_SendKeyboardStatusFunc \*sendKeyboardStatusFunc)](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_getsendkeyboardstatusfunc) | - | 从[InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md)中获取[OH\_TextEditorProxy\_SendKeyboardStatusFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_sendkeyboardstatusfunc)函数。 |
| [InputMethod\_ErrorCode OH\_TextEditorProxy\_GetSendEnterKeyFunc(InputMethod\_TextEditorProxy \*proxy, OH\_TextEditorProxy\_SendEnterKeyFunc \*sendEnterKeyFunc)](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_getsendenterkeyfunc) | - | 从[InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md)中获取[OH\_TextEditorProxy\_SendEnterKeyFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_sendenterkeyfunc)函数。 |
| [InputMethod\_ErrorCode OH\_TextEditorProxy\_GetMoveCursorFunc(InputMethod\_TextEditorProxy \*proxy, OH\_TextEditorProxy\_MoveCursorFunc \*moveCursorFunc)](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_getmovecursorfunc) | - | 从[InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md)中获取[OH\_TextEditorProxy\_MoveCursorFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_movecursorfunc)函数。 |
| [InputMethod\_ErrorCode OH\_TextEditorProxy\_GetHandleSetSelectionFunc(InputMethod\_TextEditorProxy \*proxy, OH\_TextEditorProxy\_HandleSetSelectionFunc \*handleSetSelectionFunc)](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_gethandlesetselectionfunc) | - | 从[InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md)中获取[OH\_TextEditorProxy\_HandleSetSelectionFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_handlesetselectionfunc)函数。 |
| [InputMethod\_ErrorCode OH\_TextEditorProxy\_GetHandleExtendActionFunc(InputMethod\_TextEditorProxy \*proxy, OH\_TextEditorProxy\_HandleExtendActionFunc \*handleExtendActionFunc)](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_gethandleextendactionfunc) | - | 从[InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md)中获取[OH\_TextEditorProxy\_HandleExtendActionFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_handleextendactionfunc)函数。 |
| [InputMethod\_ErrorCode OH\_TextEditorProxy\_GetGetLeftTextOfCursorFunc(InputMethod\_TextEditorProxy \*proxy, OH\_TextEditorProxy\_GetLeftTextOfCursorFunc \*getLeftTextOfCursorFunc)](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_getgetlefttextofcursorfunc) | - | 从[InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md)中获取[OH\_TextEditorProxy\_GetLeftTextOfCursorFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_getlefttextofcursorfunc)函数。 |
| [InputMethod\_ErrorCode OH\_TextEditorProxy\_GetGetRightTextOfCursorFunc(InputMethod\_TextEditorProxy \*proxy, OH\_TextEditorProxy\_GetRightTextOfCursorFunc \*getRightTextOfCursorFunc)](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_getgetrighttextofcursorfunc) | - | 从[InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md)中获取[OH\_TextEditorProxy\_GetRightTextOfCursorFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_getrighttextofcursorfunc)函数。 |
| [InputMethod\_ErrorCode OH\_TextEditorProxy\_GetGetTextIndexAtCursorFunc(InputMethod\_TextEditorProxy \*proxy, OH\_TextEditorProxy\_GetTextIndexAtCursorFunc \*getTextIndexAtCursorFunc)](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_getgettextindexatcursorfunc) | - | 从[InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md)中获取[OH\_TextEditorProxy\_GetTextIndexAtCursorFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_gettextindexatcursorfunc)函数。 |
| [InputMethod\_ErrorCode OH\_TextEditorProxy\_GetReceivePrivateCommandFunc(InputMethod\_TextEditorProxy \*proxy, OH\_TextEditorProxy\_ReceivePrivateCommandFunc \*receivePrivateCommandFunc)](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_getreceiveprivatecommandfunc) | - | 从[InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md)中获取[OH\_TextEditorProxy\_ReceivePrivateCommandFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_receiveprivatecommandfunc)函数。 |
| [InputMethod\_ErrorCode OH\_TextEditorProxy\_GetSetPreviewTextFunc(InputMethod\_TextEditorProxy \*proxy, OH\_TextEditorProxy\_SetPreviewTextFunc \*setPreviewTextFunc)](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_getsetpreviewtextfunc) | - | 从[InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md)中获取[OH\_TextEditorProxy\_SetPreviewTextFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_setpreviewtextfunc)函数。 |
| [InputMethod\_ErrorCode OH\_TextEditorProxy\_GetFinishTextPreviewFunc(InputMethod\_TextEditorProxy \*proxy, OH\_TextEditorProxy\_FinishTextPreviewFunc \*finishTextPreviewFunc)](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_getfinishtextpreviewfunc) | - | 从[InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md)中获取[OH\_TextEditorProxy\_FinishTextPreviewFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_finishtextpreviewfunc)函数。 |

## 函数说明

PhonePC/2in1TabletTVWearable

### OH\_TextEditorProxy\_GetTextConfigFunc()

PhonePC/2in1TabletTVWearable

```
1. typedef void (*OH_TextEditorProxy_GetTextConfigFunc)(InputMethod_TextEditorProxy *textEditorProxy, InputMethod_TextConfig *config)
```

**描述**

输入法获取输入框配置时触发的函数。您需要实现此函数，通过 [OH\_TextEditorProxy\_SetGetTextConfigFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_setgettextconfigfunc) 将它设置到[InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md)中， 并通过[OH\_InputMethodController\_Attach](capi-inputmethod-controller-capi-h.md#oh_inputmethodcontroller_attach)完成注册。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md) \*textEditorProxy | 指向即将被设置的[InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md)实例的指针。 |
| [InputMethod\_TextConfig](capi-inputmethod-inputmethod-textconfig.md) \*config | 表示指向[InputMethod\_TextConfig](capi-inputmethod-inputmethod-textconfig.md)实例的指针。只能在此回调接口被调用时访问该指针指向的内存，当此回调接口返回后，该内存将会被释放，不能再访问。 |

### OH\_TextEditorProxy\_InsertTextFunc()

PhonePC/2in1TabletTVWearable

```
1. typedef void (*OH_TextEditorProxy_InsertTextFunc)(InputMethod_TextEditorProxy *textEditorProxy, const char16_t *text, size_t length)
```

**描述**

输入法应用插入文本时触发的函数。您需要实现此函数，通过 [OH\_TextEditorProxy\_SetInsertTextFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_setinserttextfunc) 将它设置到[InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md)中， 并通过[OH\_InputMethodController\_Attach](capi-inputmethod-controller-capi-h.md#oh_inputmethodcontroller_attach)完成注册。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md) \*textEditorProxy | 指向即将被设置的[InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md)实例的指针。in. |
| const char16\_t \*text | 插入的字符。只能在此回调接口被调用时访问该指针指向的内存，当此回调接口返回后，该内存将会被释放，不能再访问。 |
| size\_t length | 插入字符的长度。 |

### OH\_TextEditorProxy\_DeleteForwardFunc()

PhonePC/2in1TabletTVWearable

```
1. typedef void (*OH_TextEditorProxy_DeleteForwardFunc)(InputMethod_TextEditorProxy *textEditorProxy, int32_t length)
```

**描述**

输入法删除光标右侧文本时触发的函数。您需要实现此函数，通过 [OH\_TextEditorProxy\_SetDeleteForwardFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_setdeleteforwardfunc) 将它设置到[InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md)中， 并通过[OH\_InputMethodController\_Attach](capi-inputmethod-controller-capi-h.md#oh_inputmethodcontroller_attach)完成注册。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md) \*textEditorProxy | 指向即将被设置的[InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md)实例的指针。 |
| int32\_t length | 要删除字符的长度。 |

### OH\_TextEditorProxy\_DeleteBackwardFunc()

PhonePC/2in1TabletTVWearable

```
1. typedef void (*OH_TextEditorProxy_DeleteBackwardFunc)(InputMethod_TextEditorProxy *textEditorProxy, int32_t length)
```

**描述**

输入法删除光标左侧文本时触发的函数。您需要实现此函数，通过 [OH\_TextEditorProxy\_SetDeleteBackwardFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_setdeletebackwardfunc) 将它设置到[InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md)中， 并通过[OH\_InputMethodController\_Attach](capi-inputmethod-controller-capi-h.md#oh_inputmethodcontroller_attach)完成注册。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md) \*textEditorProxy | 指向即将被设置的[InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md)实例的指针。 |
| int32\_t length | 要删除字符的长度。 |

### OH\_TextEditorProxy\_SendKeyboardStatusFunc()

PhonePC/2in1TabletTVWearable

```
1. typedef void (*OH_TextEditorProxy_SendKeyboardStatusFunc)(InputMethod_TextEditorProxy *textEditorProxy, InputMethod_KeyboardStatus keyboardStatus)
```

**描述**

输入法通知键盘状态时触发的函数。您需要实现此函数，通过 [OH\_TextEditorProxy\_SetSendKeyboardStatusFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_setsendkeyboardstatusfunc) 将它设置到[InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md)中， 并通过[OH\_InputMethodController\_Attach](capi-inputmethod-controller-capi-h.md#oh_inputmethodcontroller_attach)完成注册。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md) \*textEditorProxy | 指向即将被设置的[InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md)实例的指针。 |
| [InputMethod\_KeyboardStatus](capi-inputmethod-types-capi-h.md#inputmethod_keyboardstatus) keyboardStatus | 键盘状态，具体定义详见[InputMethod\_KeyboardStatus](capi-inputmethod-types-capi-h.md#inputmethod_keyboardstatus)。 |

### OH\_TextEditorProxy\_SendEnterKeyFunc()

PhonePC/2in1TabletTVWearable

```
1. typedef void (*OH_TextEditorProxy_SendEnterKeyFunc)(InputMethod_TextEditorProxy *textEditorProxy, InputMethod_EnterKeyType enterKeyType)
```

**描述**

输入法发送回车键时触发的函数。您需要实现此函数，通过 [OH\_TextEditorProxy\_SetSendEnterKeyFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_setsendenterkeyfunc) 将它设置到[InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md)中， 并通过[OH\_InputMethodController\_Attach](capi-inputmethod-controller-capi-h.md#oh_inputmethodcontroller_attach)完成注册。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md) \*textEditorProxy | 指向即将被设置的[InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md)实例的指针。 |
| [InputMethod\_EnterKeyType](capi-inputmethod-types-capi-h.md#inputmethod_enterkeytype) enterKeyType | 回车键类型，具体定义详见[InputMethod\_EnterKeyType](capi-inputmethod-types-capi-h.md#inputmethod_enterkeytype). |

### OH\_TextEditorProxy\_MoveCursorFunc()

PhonePC/2in1TabletTVWearable

```
1. typedef void (*OH_TextEditorProxy_MoveCursorFunc)(InputMethod_TextEditorProxy *textEditorProxy, InputMethod_Direction direction)
```

**描述**

输入法移动光标时触发的函数。您需要实现此函数，通过 [OH\_TextEditorProxy\_SetMoveCursorFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_setmovecursorfunc) 将它设置到[InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md)中， 并通过[OH\_InputMethodController\_Attach](capi-inputmethod-controller-capi-h.md#oh_inputmethodcontroller_attach)完成注册。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md) \*textEditorProxy | 指向即将被设置的[InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md)实例的指针。 |
| [InputMethod\_Direction](capi-inputmethod-types-capi-h.md#inputmethod_direction) direction | 光标移动方向，具体定义详见[InputMethod\_Direction](capi-inputmethod-types-capi-h.md#inputmethod_direction). |

### OH\_TextEditorProxy\_HandleSetSelectionFunc()

PhonePC/2in1TabletTVWearable

```
1. typedef void (*OH_TextEditorProxy_HandleSetSelectionFunc)(InputMethod_TextEditorProxy *textEditorProxy, int32_t start, int32_t end)
```

**描述**

输入法请求选中文本时触发的函数。您需要实现此函数，通过 [OH\_TextEditorProxy\_SetHandleSetSelectionFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_sethandlesetselectionfunc) 将它设置到[InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md)中， 并通过[OH\_InputMethodController\_Attach](capi-inputmethod-controller-capi-h.md#oh_inputmethodcontroller_attach)完成注册。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md) \*textEditorProxy | 指向即将被设置的[InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md)实例的指针。 |
| int32\_t start | 表示选中文本的起始位置。 |
| int32\_t end | 表示选中文本的结束位置。 |

### OH\_TextEditorProxy\_HandleExtendActionFunc()

PhonePC/2in1TabletTVWearable

```
1. typedef void (*OH_TextEditorProxy_HandleExtendActionFunc)(InputMethod_TextEditorProxy *textEditorProxy, InputMethod_ExtendAction action)
```

**描述**

输入法发送扩展编辑操作时触发的函数。您需要实现此函数，通过 [OH\_TextEditorProxy\_SetHandleExtendActionFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_sethandleextendactionfunc) 将它设置到[InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md)中， 并通过[OH\_InputMethodController\_Attach](capi-inputmethod-controller-capi-h.md#oh_inputmethodcontroller_attach)完成注册。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md) \*textEditorProxy | 指向即将被设置的[InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md)实例的指针。 |
| [InputMethod\_ExtendAction](capi-inputmethod-types-capi-h.md#inputmethod_extendaction) action | 扩展编辑操作，具体定义详见[InputMethod\_ExtendAction](capi-inputmethod-types-capi-h.md#inputmethod_extendaction). |

### OH\_TextEditorProxy\_GetLeftTextOfCursorFunc()

PhonePC/2in1TabletTVWearable

```
1. typedef void (*OH_TextEditorProxy_GetLeftTextOfCursorFunc)(InputMethod_TextEditorProxy *textEditorProxy, int32_t number, char16_t text[], size_t *length)
```

**描述**

输入法获取光标左侧文本时触发的函数。您需要实现此函数，通过 [OH\_TextEditorProxy\_SetGetLeftTextOfCursorFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_setgetlefttextofcursorfunc) 将它设置到[InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md)中， 并通过[OH\_InputMethodController\_Attach](capi-inputmethod-controller-capi-h.md#oh_inputmethodcontroller_attach)完成注册。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md) \*textEditorProxy | 指向即将被设置的[InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md)实例的指针。 |
| int32\_t number | 目标获取文本的长度。 |
| char16\_t text[] | 光标左侧指定长度的文本内容，需要在函数实现中对它赋值。只能在此回调接口被调用时访问该指针指向的内存，当此回调接口返回后，该内存将会被释放，不能再访问。 |
| size\_t \*length | 表示游标左侧文本的长度，您需要传递此参数。 |

### OH\_TextEditorProxy\_GetRightTextOfCursorFunc()

PhonePC/2in1TabletTVWearable

```
1. typedef void (*OH_TextEditorProxy_GetRightTextOfCursorFunc)(InputMethod_TextEditorProxy *textEditorProxy, int32_t number, char16_t text[], size_t *length)
```

**描述**

输入法获取光标右侧文本时触发的函数。您需要实现此函数，通过 [OH\_TextEditorProxy\_SetGetRightTextOfCursorFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_setgetrighttextofcursorfunc) 将它设置到[InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md)中， 并通过[OH\_InputMethodController\_Attach](capi-inputmethod-controller-capi-h.md#oh_inputmethodcontroller_attach)完成注册。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md) \*textEditorProxy | 指向即将被设置的[InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md)实例的指针。 |
| int32\_t number | 目标获取文本的长度。 |
| char16\_t text[] | 光标右侧指定长度的文本内容，需要在函数实现中对它赋值。只能在此回调接口被调用时访问该指针指向的内存，当此回调接口返回后，该内存将会被释放，不能再访问。 |
| size\_t \*length | 表示游标右侧文本的长度，您需要传递此参数。 |

### OH\_TextEditorProxy\_GetTextIndexAtCursorFunc()

PhonePC/2in1TabletTVWearable

```
1. typedef int32_t (*OH_TextEditorProxy_GetTextIndexAtCursorFunc)(InputMethod_TextEditorProxy *textEditorProxy)
```

**描述**

输入法获取光标所在输入框文本索引时触发的函数。您需要实现此函数，通过 [OH\_TextEditorProxy\_SetGetTextIndexAtCursorFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_setgettextindexatcursorfunc) 将它设置到[InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md)中， 并通过[OH\_InputMethodController\_Attach](capi-inputmethod-controller-capi-h.md#oh_inputmethodcontroller_attach)完成注册。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md) \*textEditorProxy | 指向即将被设置的[InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md)实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回光标所在输入框文本索引。 |

### OH\_TextEditorProxy\_ReceivePrivateCommandFunc()

PhonePC/2in1TabletTVWearable

```
1. typedef int32_t (*OH_TextEditorProxy_ReceivePrivateCommandFunc)(InputMethod_TextEditorProxy *textEditorProxy, InputMethod_PrivateCommand *privateCommand[], size_t size)
```

**描述**

输入法应用发送私有数据命令时触发的函数。您需要实现此函数，通过 [OH\_TextEditorProxy\_SetReceivePrivateCommandFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_setreceiveprivatecommandfunc) 将它设置到[InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md)中， 并通过[OH\_InputMethodController\_Attach](capi-inputmethod-controller-capi-h.md#oh_inputmethodcontroller_attach)完成注册。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md) \*textEditorProxy | 指向即将被设置的[InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md)实例的指针。 |
| [InputMethod\_PrivateCommand](capi-inputmethod-inputmethod-privatecommand.md) \*privateCommand[] | 私有数据命令。只能在此回调接口被调用时访问该指针指向的内存，当此回调接口返回后，该内存将会被释放，不能再访问。 |
| size\_t size | 私有数据的大小。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回对私有数据命令处理的处理结果。 |

### OH\_TextEditorProxy\_SetPreviewTextFunc()

PhonePC/2in1TabletTVWearable

```
1. typedef int32_t (*OH_TextEditorProxy_SetPreviewTextFunc)(InputMethod_TextEditorProxy *textEditorProxy, const char16_t text[], size_t length, int32_t start, int32_t end)
```

**描述**

输入法设置预上屏文本时触发的函数。您需要实现此函数，通过 [OH\_TextEditorProxy\_SetSetPreviewTextFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_setsetpreviewtextfunc) 将它设置到[InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md)中， 并通过[OH\_InputMethodController\_Attach](capi-inputmethod-controller-capi-h.md#oh_inputmethodcontroller_attach)完成注册。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md) \*textEditorProxy | 指向即将被设置的[InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md)实例的指针。 |
| const char16\_t text[] | 请求设置为预上屏样式的文本内容。只能在此回调接口被调用时访问该指针指向的内存，当此回调接口返回后，该内存将会被释放，不能再访问。 |
| size\_t length | 预上屏文本长度。 |
| int32\_t start | 预上屏文本起始光标位置。 |
| int32\_t end | 预上屏文本结束光标位置。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回设置预上屏文本的处理结果。 |

### OH\_TextEditorProxy\_FinishTextPreviewFunc()

PhonePC/2in1TabletTVWearable

```
1. typedef void (*OH_TextEditorProxy_FinishTextPreviewFunc)(InputMethod_TextEditorProxy *textEditorProxy)
```

**描述**

输入法结束预上屏时触发的函数。您需要实现此函数，通过 [OH\_TextEditorProxy\_SetFinishTextPreviewFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_setfinishtextpreviewfunc) 将它设置到[InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md)中， 并通过[OH\_InputMethodController\_Attach](capi-inputmethod-controller-capi-h.md#oh_inputmethodcontroller_attach)完成注册。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md) \*textEditorProxy | 指向即将被设置的[InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md)实例的指针。 |

### OH\_TextEditorProxy\_Create()

PhonePC/2in1TabletTVWearable

```
1. InputMethod_TextEditorProxy *OH_TextEditorProxy_Create(void)
```

**描述**

创建一个新的[InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md)实例。

**起始版本：** 12

**返回：**

| 类型 | 说明 |
| --- | --- |
| [InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md) \* | 如果创建成功，返回一个指向新创建的[InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md)实例的指针。  如果创建失败，对象返回NULL，可能的失败原因有应用地址空间满。 |

### OH\_TextEditorProxy\_Destroy()

PhonePC/2in1TabletTVWearable

```
1. void OH_TextEditorProxy_Destroy(InputMethod_TextEditorProxy *proxy)
```

**描述**

销毁一个[InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md)实例。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md) \*proxy | 表示指向即将被销毁的[InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md)实例的指针。 |

### OH\_TextEditorProxy\_SetGetTextConfigFunc()

PhonePC/2in1TabletTVWearable

```
1. InputMethod_ErrorCode OH_TextEditorProxy_SetGetTextConfigFunc(InputMethod_TextEditorProxy *proxy, OH_TextEditorProxy_GetTextConfigFunc getTextConfigFunc)
```

**描述**

将函数[OH\_TextEditorProxy\_GetTextConfigFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_gettextconfigfunc)设置到[InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md)中。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md) \*proxy | 指向即将被设置的[InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md)实例的指针。 |
| [OH\_TextEditorProxy\_GetTextConfigFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_gettextconfigfunc) getTextConfigFunc | 表示被设置到proxy的函数[OH\_TextEditorProxy\_GetTextConfigFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_gettextconfigfunc)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [InputMethod\_ErrorCode](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) | 返回一个特定的错误码。  [IME\_ERR\_OK](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 表示成功。  [IME\_ERR\_NULL\_POINTER](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 非预期的空指针。  具体错误码可以参考 [InputMethod\_ErrorCode](capi-inputmethod-types-capi-h.md#inputmethod_errorcode)。 |

### OH\_TextEditorProxy\_SetInsertTextFunc()

PhonePC/2in1TabletTVWearable

```
1. InputMethod_ErrorCode OH_TextEditorProxy_SetInsertTextFunc(InputMethod_TextEditorProxy *proxy, OH_TextEditorProxy_InsertTextFunc insertTextFunc)
```

**描述**

将函数[OH\_TextEditorProxy\_InsertTextFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_inserttextfunc)设置到[InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md)中。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md) \*proxy | 指向即将被设置的[InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md)实例的指针。 |
| [OH\_TextEditorProxy\_InsertTextFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_inserttextfunc) insertTextFunc | 表示被设置到proxy的函数[OH\_TextEditorProxy\_InsertTextFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_inserttextfunc)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [InputMethod\_ErrorCode](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) | 返回一个特定的错误码。  [IME\_ERR\_OK](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 表示成功。  [IME\_ERR\_NULL\_POINTER](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 非预期的空指针。  具体错误码可以参考 [InputMethod\_ErrorCode](capi-inputmethod-types-capi-h.md#inputmethod_errorcode)。 |

### OH\_TextEditorProxy\_SetDeleteForwardFunc()

PhonePC/2in1TabletTVWearable

```
1. InputMethod_ErrorCode OH_TextEditorProxy_SetDeleteForwardFunc(InputMethod_TextEditorProxy *proxy, OH_TextEditorProxy_DeleteForwardFunc deleteForwardFunc)
```

**描述**

将函数[OH\_TextEditorProxy\_DeleteForwardFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_deleteforwardfunc)设置到[InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md)中。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md) \*proxy | 指向即将被设置的[InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md)实例的指针。 |
| [OH\_TextEditorProxy\_DeleteForwardFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_deleteforwardfunc) deleteForwardFunc | 表示被设置到proxy的函数[OH\_TextEditorProxy\_DeleteForwardFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_deleteforwardfunc)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [InputMethod\_ErrorCode](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) | 返回一个特定的错误码。  [IME\_ERR\_OK](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 表示成功。  [IME\_ERR\_NULL\_POINTER](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 非预期的空指针。  具体错误码可以参考 [InputMethod\_ErrorCode](capi-inputmethod-types-capi-h.md#inputmethod_errorcode)。 |

### OH\_TextEditorProxy\_SetDeleteBackwardFunc()

PhonePC/2in1TabletTVWearable

```
1. InputMethod_ErrorCode OH_TextEditorProxy_SetDeleteBackwardFunc(InputMethod_TextEditorProxy *proxy, OH_TextEditorProxy_DeleteBackwardFunc deleteBackwardFunc)
```

**描述**

将函数[OH\_TextEditorProxy\_DeleteBackwardFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_deletebackwardfunc)设置到[InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md)中。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md) \*proxy | 指向即将被设置的[InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md)实例的指针。 |
| [OH\_TextEditorProxy\_DeleteBackwardFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_deletebackwardfunc) deleteBackwardFunc | 表示被设置到proxy的函数[OH\_TextEditorProxy\_DeleteBackwardFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_deletebackwardfunc)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [InputMethod\_ErrorCode](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) | 返回一个特定的错误码。  [IME\_ERR\_OK](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 表示成功。  [IME\_ERR\_NULL\_POINTER](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 非预期的空指针。  具体错误码可以参考 [InputMethod\_ErrorCode](capi-inputmethod-types-capi-h.md#inputmethod_errorcode)。 |

### OH\_TextEditorProxy\_SetSendKeyboardStatusFunc()

PhonePC/2in1TabletTVWearable

```
1. InputMethod_ErrorCode OH_TextEditorProxy_SetSendKeyboardStatusFunc(InputMethod_TextEditorProxy *proxy, OH_TextEditorProxy_SendKeyboardStatusFunc sendKeyboardStatusFunc)
```

**描述**

将函数[OH\_TextEditorProxy\_SendKeyboardStatusFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_sendkeyboardstatusfunc)设置到[InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md)中。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md) \*proxy | 指向即将被设置的[InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md)实例的指针。 |
| [OH\_TextEditorProxy\_SendKeyboardStatusFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_sendkeyboardstatusfunc) sendKeyboardStatusFunc | 表示被设置到proxy的函数[OH\_TextEditorProxy\_SendKeyboardStatusFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_sendkeyboardstatusfunc)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [InputMethod\_ErrorCode](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) | 返回一个特定的错误码。  [IME\_ERR\_OK](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 表示成功。  [IME\_ERR\_NULL\_POINTER](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 非预期的空指针。  具体错误码可以参考 [InputMethod\_ErrorCode](capi-inputmethod-types-capi-h.md#inputmethod_errorcode)。 |

### OH\_TextEditorProxy\_SetSendEnterKeyFunc()

PhonePC/2in1TabletTVWearable

```
1. InputMethod_ErrorCode OH_TextEditorProxy_SetSendEnterKeyFunc(InputMethod_TextEditorProxy *proxy, OH_TextEditorProxy_SendEnterKeyFunc sendEnterKeyFunc)
```

**描述**

将函数[OH\_TextEditorProxy\_SetSendEnterKeyFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_setsendenterkeyfunc)设置到[InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md)中。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md) \*proxy | 指向即将被设置的[InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md)实例的指针。 |
| [OH\_TextEditorProxy\_SendEnterKeyFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_sendenterkeyfunc) sendEnterKeyFunc | 表示被设置到proxy的函数[OH\_TextEditorProxy\_SendEnterKeyFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_sendenterkeyfunc)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [InputMethod\_ErrorCode](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) | 返回一个特定的错误码。  [IME\_ERR\_OK](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 表示成功。  [IME\_ERR\_NULL\_POINTER](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 非预期的空指针。  具体错误码可以参考 [InputMethod\_ErrorCode](capi-inputmethod-types-capi-h.md#inputmethod_errorcode)。 |

### OH\_TextEditorProxy\_SetMoveCursorFunc()

PhonePC/2in1TabletTVWearable

```
1. InputMethod_ErrorCode OH_TextEditorProxy_SetMoveCursorFunc(InputMethod_TextEditorProxy *proxy, OH_TextEditorProxy_MoveCursorFunc moveCursorFunc)
```

**描述**

将函数[OH\_TextEditorProxy\_SetMoveCursorFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_setmovecursorfunc)设置到[InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md)中。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md) \*proxy | 指向即将被设置的[InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md)实例的指针。 |
| [OH\_TextEditorProxy\_MoveCursorFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_movecursorfunc) moveCursorFunc | 表示被设置到proxy的函数[OH\_TextEditorProxy\_MoveCursorFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_movecursorfunc)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [InputMethod\_ErrorCode](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) | 返回一个特定的错误码。  [IME\_ERR\_OK](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 表示成功。  [IME\_ERR\_NULL\_POINTER](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 非预期的空指针。  具体错误码可以参考 [InputMethod\_ErrorCode](capi-inputmethod-types-capi-h.md#inputmethod_errorcode)。 |

### OH\_TextEditorProxy\_SetHandleSetSelectionFunc()

PhonePC/2in1TabletTVWearable

```
1. InputMethod_ErrorCode OH_TextEditorProxy_SetHandleSetSelectionFunc(InputMethod_TextEditorProxy *proxy, OH_TextEditorProxy_HandleSetSelectionFunc handleSetSelectionFunc)
```

**描述**

将函数[OH\_TextEditorProxy\_HandleSetSelectionFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_handlesetselectionfunc)设置到[InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md)中。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md) \*proxy | 指向即将被设置的[InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md)实例的指针。 |
| [OH\_TextEditorProxy\_HandleSetSelectionFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_handlesetselectionfunc) handleSetSelectionFunc | 表示被设置到proxy的函数[OH\_TextEditorProxy\_HandleSetSelectionFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_handlesetselectionfunc)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [InputMethod\_ErrorCode](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) | 返回一个特定的错误码。  [IME\_ERR\_OK](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 表示成功。  [IME\_ERR\_NULL\_POINTER](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 非预期的空指针。  具体错误码可以参考 [InputMethod\_ErrorCode](capi-inputmethod-types-capi-h.md#inputmethod_errorcode)。 |

### OH\_TextEditorProxy\_SetHandleExtendActionFunc()

PhonePC/2in1TabletTVWearable

```
1. InputMethod_ErrorCode OH_TextEditorProxy_SetHandleExtendActionFunc(InputMethod_TextEditorProxy *proxy, OH_TextEditorProxy_HandleExtendActionFunc handleExtendActionFunc)
```

**描述**

将函数[OH\_TextEditorProxy\_HandleExtendActionFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_handleextendactionfunc)设置到[InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md)中。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md) \*proxy | 指向即将被设置的[InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md)实例的指针。 |
| [OH\_TextEditorProxy\_HandleExtendActionFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_handleextendactionfunc) handleExtendActionFunc | 表示被设置到proxy的函数[OH\_TextEditorProxy\_HandleExtendActionFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_handleextendactionfunc)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [InputMethod\_ErrorCode](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) | 返回一个特定的错误码。  [IME\_ERR\_OK](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 表示成功。  [IME\_ERR\_NULL\_POINTER](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 非预期的空指针。  具体错误码可以参考 [InputMethod\_ErrorCode](capi-inputmethod-types-capi-h.md#inputmethod_errorcode)。 |

### OH\_TextEditorProxy\_SetGetLeftTextOfCursorFunc()

PhonePC/2in1TabletTVWearable

```
1. InputMethod_ErrorCode OH_TextEditorProxy_SetGetLeftTextOfCursorFunc(InputMethod_TextEditorProxy *proxy, OH_TextEditorProxy_GetLeftTextOfCursorFunc getLeftTextOfCursorFunc)
```

**描述**

将函数[OH\_TextEditorProxy\_GetLeftTextOfCursorFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_getlefttextofcursorfunc)设置到[InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md)中。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md) \*proxy | 指向即将被设置的[InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md)实例的指针。 |
| [OH\_TextEditorProxy\_GetLeftTextOfCursorFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_getlefttextofcursorfunc) getLeftTextOfCursorFunc | 表示被设置到proxy的函数[OH\_TextEditorProxy\_GetLeftTextOfCursorFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_getlefttextofcursorfunc)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [InputMethod\_ErrorCode](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) | 返回一个特定的错误码。  [IME\_ERR\_OK](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 表示成功。  [IME\_ERR\_NULL\_POINTER](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 非预期的空指针。  具体错误码可以参考 [InputMethod\_ErrorCode](capi-inputmethod-types-capi-h.md#inputmethod_errorcode)。 |

### OH\_TextEditorProxy\_SetGetRightTextOfCursorFunc()

PhonePC/2in1TabletTVWearable

```
1. InputMethod_ErrorCode OH_TextEditorProxy_SetGetRightTextOfCursorFunc(InputMethod_TextEditorProxy *proxy, OH_TextEditorProxy_GetRightTextOfCursorFunc getRightTextOfCursorFunc)
```

**描述**

将函数[OH\_TextEditorProxy\_GetRightTextOfCursorFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_getrighttextofcursorfunc)设置到[InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md)中。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md) \*proxy | 指向即将被设置的[InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md)实例的指针。 |
| [OH\_TextEditorProxy\_GetRightTextOfCursorFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_getrighttextofcursorfunc) getRightTextOfCursorFunc | 表示被设置到proxy的函数[OH\_TextEditorProxy\_GetRightTextOfCursorFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_getrighttextofcursorfunc)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [InputMethod\_ErrorCode](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) | 返回一个特定的错误码。  [IME\_ERR\_OK](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 表示成功。  [IME\_ERR\_NULL\_POINTER](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 非预期的空指针。  具体错误码可以参考 [InputMethod\_ErrorCode](capi-inputmethod-types-capi-h.md#inputmethod_errorcode)。 |

### OH\_TextEditorProxy\_SetGetTextIndexAtCursorFunc()

PhonePC/2in1TabletTVWearable

```
1. InputMethod_ErrorCode OH_TextEditorProxy_SetGetTextIndexAtCursorFunc(InputMethod_TextEditorProxy *proxy, OH_TextEditorProxy_GetTextIndexAtCursorFunc getTextIndexAtCursorFunc)
```

**描述**

将函数[OH\_TextEditorProxy\_GetTextIndexAtCursorFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_gettextindexatcursorfunc)设置到[InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md)中。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md) \*proxy | 指向即将被设置的[InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md)实例的指针。 |
| [OH\_TextEditorProxy\_GetTextIndexAtCursorFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_gettextindexatcursorfunc) getTextIndexAtCursorFunc | 表示被设置到proxy的函数[OH\_TextEditorProxy\_GetTextIndexAtCursorFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_gettextindexatcursorfunc)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [InputMethod\_ErrorCode](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) | 返回一个特定的错误码。  [IME\_ERR\_OK](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 表示成功。  [IME\_ERR\_NULL\_POINTER](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 非预期的空指针。  具体错误码可以参考 [InputMethod\_ErrorCode](capi-inputmethod-types-capi-h.md#inputmethod_errorcode)。 |

### OH\_TextEditorProxy\_SetReceivePrivateCommandFunc()

PhonePC/2in1TabletTVWearable

```
1. InputMethod_ErrorCode OH_TextEditorProxy_SetReceivePrivateCommandFunc(InputMethod_TextEditorProxy *proxy, OH_TextEditorProxy_ReceivePrivateCommandFunc receivePrivateCommandFunc)
```

**描述**

将函数[OH\_TextEditorProxy\_ReceivePrivateCommandFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_receiveprivatecommandfunc)设置到[InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md)中。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md) \*proxy | 指向即将被设置的[InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md)实例的指针。 |
| [OH\_TextEditorProxy\_ReceivePrivateCommandFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_receiveprivatecommandfunc) receivePrivateCommandFunc | 表示被设置到proxy的函数[OH\_TextEditorProxy\_ReceivePrivateCommandFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_receiveprivatecommandfunc)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [InputMethod\_ErrorCode](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) | 返回一个特定的错误码。  [IME\_ERR\_OK](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 表示成功。  [IME\_ERR\_NULL\_POINTER](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 非预期的空指针。  具体错误码可以参考 [InputMethod\_ErrorCode](capi-inputmethod-types-capi-h.md#inputmethod_errorcode)。 |

### OH\_TextEditorProxy\_SetSetPreviewTextFunc()

PhonePC/2in1TabletTVWearable

```
1. InputMethod_ErrorCode OH_TextEditorProxy_SetSetPreviewTextFunc(InputMethod_TextEditorProxy *proxy, OH_TextEditorProxy_SetPreviewTextFunc setPreviewTextFunc)
```

**描述**

将函数[OH\_TextEditorProxy\_SetPreviewTextFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_setpreviewtextfunc)设置到[InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md)中。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md) \*proxy | 指向即将被设置的[InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md)实例的指针。 |
| [OH\_TextEditorProxy\_SetPreviewTextFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_setpreviewtextfunc) setPreviewTextFunc | 表示被设置到proxy的函数[OH\_TextEditorProxy\_SetPreviewTextFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_setpreviewtextfunc)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [InputMethod\_ErrorCode](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) | 返回一个特定的错误码。  [IME\_ERR\_OK](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 表示成功。  [IME\_ERR\_NULL\_POINTER](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 非预期的空指针。  具体错误码可以参考 [InputMethod\_ErrorCode](capi-inputmethod-types-capi-h.md#inputmethod_errorcode)。 |

### OH\_TextEditorProxy\_SetFinishTextPreviewFunc()

PhonePC/2in1TabletTVWearable

```
1. InputMethod_ErrorCode OH_TextEditorProxy_SetFinishTextPreviewFunc(InputMethod_TextEditorProxy *proxy, OH_TextEditorProxy_FinishTextPreviewFunc finishTextPreviewFunc)
```

**描述**

将函数[OH\_TextEditorProxy\_FinishTextPreviewFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_finishtextpreviewfunc)设置到[InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md)中。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md) \*proxy | 指向即将被设置的[InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md)实例的指针。 |
| [OH\_TextEditorProxy\_FinishTextPreviewFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_finishtextpreviewfunc) finishTextPreviewFunc | 表示被设置到proxy的函数[OH\_TextEditorProxy\_FinishTextPreviewFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_finishtextpreviewfunc)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [InputMethod\_ErrorCode](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) | 返回一个特定的错误码。  [IME\_ERR\_OK](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 表示成功。  [IME\_ERR\_NULL\_POINTER](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 非预期的空指针。  具体错误码可以参考 [InputMethod\_ErrorCode](capi-inputmethod-types-capi-h.md#inputmethod_errorcode)。 |

### OH\_TextEditorProxy\_GetGetTextConfigFunc()

PhonePC/2in1TabletTVWearable

```
1. InputMethod_ErrorCode OH_TextEditorProxy_GetGetTextConfigFunc(InputMethod_TextEditorProxy *proxy, OH_TextEditorProxy_GetTextConfigFunc *getTextConfigFunc)
```

**描述**

从[InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md)中获取[OH\_TextEditorProxy\_GetTextConfigFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_gettextconfigfunc)函数。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md) \*proxy | 指向被读取的[InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md)实例的指针。 |
| [OH\_TextEditorProxy\_GetTextConfigFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_gettextconfigfunc) \*getTextConfigFunc | 表示从proxy获取到的函数[OH\_TextEditorProxy\_GetTextConfigFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_gettextconfigfunc)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [InputMethod\_ErrorCode](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) | 返回一个特定的错误码。  [IME\_ERR\_OK](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 表示成功。  [IME\_ERR\_NULL\_POINTER](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 非预期的空指针。  具体错误码可以参考 [InputMethod\_ErrorCode](capi-inputmethod-types-capi-h.md#inputmethod_errorcode)。 |

### OH\_TextEditorProxy\_GetInsertTextFunc()

PhonePC/2in1TabletTVWearable

```
1. InputMethod_ErrorCode OH_TextEditorProxy_GetInsertTextFunc(InputMethod_TextEditorProxy *proxy, OH_TextEditorProxy_InsertTextFunc *insertTextFunc)
```

**描述**

从[InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md)中获取[OH\_TextEditorProxy\_InsertTextFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_inserttextfunc)函数。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md) \*proxy | 指向被读取的[InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md)实例的指针。 |
| [OH\_TextEditorProxy\_InsertTextFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_inserttextfunc) \*insertTextFunc | 表示从proxy获取到的函数[OH\_TextEditorProxy\_InsertTextFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_inserttextfunc)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [InputMethod\_ErrorCode](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) | 返回一个特定的错误码。  [IME\_ERR\_OK](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 表示成功。  [IME\_ERR\_NULL\_POINTER](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 非预期的空指针。  具体错误码可以参考 [InputMethod\_ErrorCode](capi-inputmethod-types-capi-h.md#inputmethod_errorcode)。 |

### OH\_TextEditorProxy\_GetDeleteForwardFunc()

PhonePC/2in1TabletTVWearable

```
1. InputMethod_ErrorCode OH_TextEditorProxy_GetDeleteForwardFunc(InputMethod_TextEditorProxy *proxy, OH_TextEditorProxy_DeleteForwardFunc *deleteForwardFunc)
```

**描述**

从[InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md)中获取[OH\_TextEditorProxy\_DeleteForwardFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_deleteforwardfunc)函数。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md) \*proxy | 指向被读取的[InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md)实例的指针。 |
| [OH\_TextEditorProxy\_DeleteForwardFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_deleteforwardfunc) \*deleteForwardFunc | 表示从proxy获取到的函数[OH\_TextEditorProxy\_DeleteForwardFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_deleteforwardfunc)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [InputMethod\_ErrorCode](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) | 返回一个特定的错误码。  [IME\_ERR\_OK](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 表示成功。  [IME\_ERR\_NULL\_POINTER](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 非预期的空指针。  具体错误码可以参考 [InputMethod\_ErrorCode](capi-inputmethod-types-capi-h.md#inputmethod_errorcode)。 |

### OH\_TextEditorProxy\_GetDeleteBackwardFunc()

PhonePC/2in1TabletTVWearable

```
1. InputMethod_ErrorCode OH_TextEditorProxy_GetDeleteBackwardFunc(InputMethod_TextEditorProxy *proxy, OH_TextEditorProxy_DeleteBackwardFunc *deleteBackwardFunc)
```

**描述**

从[InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md)中获取[OH\_TextEditorProxy\_DeleteBackwardFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_deletebackwardfunc)函数。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md) \*proxy | 指向被读取的[InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md)实例的指针。 |
| [OH\_TextEditorProxy\_DeleteBackwardFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_deletebackwardfunc) \*deleteBackwardFunc | 表示从proxy获取到的函数[OH\_TextEditorProxy\_DeleteBackwardFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_deletebackwardfunc)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [InputMethod\_ErrorCode](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) | 返回一个特定的错误码。  [IME\_ERR\_OK](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 表示成功。  [IME\_ERR\_NULL\_POINTER](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 非预期的空指针。  具体错误码可以参考 [InputMethod\_ErrorCode](capi-inputmethod-types-capi-h.md#inputmethod_errorcode)。 |

### OH\_TextEditorProxy\_GetSendKeyboardStatusFunc()

PhonePC/2in1TabletTVWearable

```
1. InputMethod_ErrorCode OH_TextEditorProxy_GetSendKeyboardStatusFunc(InputMethod_TextEditorProxy *proxy, OH_TextEditorProxy_SendKeyboardStatusFunc *sendKeyboardStatusFunc)
```

**描述**

从[InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md)中获取[OH\_TextEditorProxy\_SendKeyboardStatusFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_sendkeyboardstatusfunc)函数。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md) \*proxy | 指向被读取的[InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md)实例的指针。 |
| [OH\_TextEditorProxy\_SendKeyboardStatusFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_sendkeyboardstatusfunc) \*sendKeyboardStatusFunc | 表示从proxy获取到的函数[OH\_TextEditorProxy\_SendKeyboardStatusFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_sendkeyboardstatusfunc)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [InputMethod\_ErrorCode](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) | 返回一个特定的错误码。  [IME\_ERR\_OK](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 表示成功。  [IME\_ERR\_NULL\_POINTER](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 非预期的空指针。  具体错误码可以参考 [InputMethod\_ErrorCode](capi-inputmethod-types-capi-h.md#inputmethod_errorcode)。 |

### OH\_TextEditorProxy\_GetSendEnterKeyFunc()

PhonePC/2in1TabletTVWearable

```
1. InputMethod_ErrorCode OH_TextEditorProxy_GetSendEnterKeyFunc(InputMethod_TextEditorProxy *proxy, OH_TextEditorProxy_SendEnterKeyFunc *sendEnterKeyFunc)
```

**描述**

从[InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md)中获取[OH\_TextEditorProxy\_SendEnterKeyFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_sendenterkeyfunc)函数。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md) \*proxy | 指向被读取的[InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md)实例的指针。 |
| [OH\_TextEditorProxy\_SendEnterKeyFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_sendenterkeyfunc) \*sendEnterKeyFunc | 表示从proxy获取到的函数[OH\_TextEditorProxy\_SendEnterKeyFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_sendenterkeyfunc)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [InputMethod\_ErrorCode](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) | 返回一个特定的错误码。  [IME\_ERR\_OK](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 表示成功。  [IME\_ERR\_NULL\_POINTER](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 非预期的空指针。  具体错误码可以参考 [InputMethod\_ErrorCode](capi-inputmethod-types-capi-h.md#inputmethod_errorcode)。 |

### OH\_TextEditorProxy\_GetMoveCursorFunc()

PhonePC/2in1TabletTVWearable

```
1. InputMethod_ErrorCode OH_TextEditorProxy_GetMoveCursorFunc(InputMethod_TextEditorProxy *proxy, OH_TextEditorProxy_MoveCursorFunc *moveCursorFunc)
```

**描述**

从[InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md)中获取[OH\_TextEditorProxy\_MoveCursorFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_movecursorfunc)函数。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md) \*proxy | 指向被读取的[InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md)实例的指针。 |
| [OH\_TextEditorProxy\_MoveCursorFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_movecursorfunc) \*moveCursorFunc | 表示从proxy获取到的函数[OH\_TextEditorProxy\_MoveCursorFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_movecursorfunc)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [InputMethod\_ErrorCode](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) | 返回一个特定的错误码。  [IME\_ERR\_OK](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 表示成功。  [IME\_ERR\_NULL\_POINTER](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 非预期的空指针。  具体错误码可以参考 [InputMethod\_ErrorCode](capi-inputmethod-types-capi-h.md#inputmethod_errorcode)。 |

### OH\_TextEditorProxy\_GetHandleSetSelectionFunc()

PhonePC/2in1TabletTVWearable

```
1. InputMethod_ErrorCode OH_TextEditorProxy_GetHandleSetSelectionFunc(InputMethod_TextEditorProxy *proxy, OH_TextEditorProxy_HandleSetSelectionFunc *handleSetSelectionFunc)
```

**描述**

从[InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md)中获取[OH\_TextEditorProxy\_HandleSetSelectionFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_handlesetselectionfunc)函数。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md) \*proxy | 指向被读取的[InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md)实例的指针。 |
| [OH\_TextEditorProxy\_HandleSetSelectionFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_handlesetselectionfunc) \*handleSetSelectionFunc | 表示从proxy获取到的函数[OH\_TextEditorProxy\_HandleSetSelectionFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_handlesetselectionfunc)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [InputMethod\_ErrorCode](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) | 返回一个特定的错误码。  [IME\_ERR\_OK](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 表示成功。  [IME\_ERR\_NULL\_POINTER](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 非预期的空指针。  具体错误码可以参考 [InputMethod\_ErrorCode](capi-inputmethod-types-capi-h.md#inputmethod_errorcode)。 |

### OH\_TextEditorProxy\_GetHandleExtendActionFunc()

PhonePC/2in1TabletTVWearable

```
1. InputMethod_ErrorCode OH_TextEditorProxy_GetHandleExtendActionFunc(InputMethod_TextEditorProxy *proxy, OH_TextEditorProxy_HandleExtendActionFunc *handleExtendActionFunc)
```

**描述**

从[InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md)中获取[OH\_TextEditorProxy\_HandleExtendActionFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_handleextendactionfunc)函数。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md) \*proxy | 指向被读取的[InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md)实例的指针。 |
| [OH\_TextEditorProxy\_HandleExtendActionFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_handleextendactionfunc) \*handleExtendActionFunc | 表示从proxy获取到的函数[OH\_TextEditorProxy\_HandleExtendActionFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_handleextendactionfunc)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [InputMethod\_ErrorCode](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) | 返回一个特定的错误码。  [IME\_ERR\_OK](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 表示成功。  [IME\_ERR\_NULL\_POINTER](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 非预期的空指针。  具体错误码可以参考 [InputMethod\_ErrorCode](capi-inputmethod-types-capi-h.md#inputmethod_errorcode)。 |

### OH\_TextEditorProxy\_GetGetLeftTextOfCursorFunc()

PhonePC/2in1TabletTVWearable

```
1. InputMethod_ErrorCode OH_TextEditorProxy_GetGetLeftTextOfCursorFunc(InputMethod_TextEditorProxy *proxy, OH_TextEditorProxy_GetLeftTextOfCursorFunc *getLeftTextOfCursorFunc)
```

**描述**

从[InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md)中获取[OH\_TextEditorProxy\_GetLeftTextOfCursorFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_getlefttextofcursorfunc)函数。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md) \*proxy | 指向被读取的[InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md)实例的指针。 |
| [OH\_TextEditorProxy\_GetLeftTextOfCursorFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_getlefttextofcursorfunc) \*getLeftTextOfCursorFunc | 表示从proxy获取到的函数[OH\_TextEditorProxy\_GetLeftTextOfCursorFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_getlefttextofcursorfunc)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [InputMethod\_ErrorCode](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) | 返回一个特定的错误码。  [IME\_ERR\_OK](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 表示成功。  [IME\_ERR\_NULL\_POINTER](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 非预期的空指针。  具体错误码可以参考 [InputMethod\_ErrorCode](capi-inputmethod-types-capi-h.md#inputmethod_errorcode)。 |

### OH\_TextEditorProxy\_GetGetRightTextOfCursorFunc()

PhonePC/2in1TabletTVWearable

```
1. InputMethod_ErrorCode OH_TextEditorProxy_GetGetRightTextOfCursorFunc(InputMethod_TextEditorProxy *proxy, OH_TextEditorProxy_GetRightTextOfCursorFunc *getRightTextOfCursorFunc)
```

**描述**

从[InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md)中获取[OH\_TextEditorProxy\_GetRightTextOfCursorFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_getrighttextofcursorfunc)函数。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md) \*proxy | 指向被读取的[InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md)实例的指针。 |
| [OH\_TextEditorProxy\_GetRightTextOfCursorFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_getrighttextofcursorfunc) \*getRightTextOfCursorFunc | 表示从proxy获取到的函数[OH\_TextEditorProxy\_GetRightTextOfCursorFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_getrighttextofcursorfunc)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [InputMethod\_ErrorCode](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) | 返回一个特定的错误码。  [IME\_ERR\_OK](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 表示成功。  [IME\_ERR\_NULL\_POINTER](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 非预期的空指针。  具体错误码可以参考 [InputMethod\_ErrorCode](capi-inputmethod-types-capi-h.md#inputmethod_errorcode)。 |

### OH\_TextEditorProxy\_GetGetTextIndexAtCursorFunc()

PhonePC/2in1TabletTVWearable

```
1. InputMethod_ErrorCode OH_TextEditorProxy_GetGetTextIndexAtCursorFunc(InputMethod_TextEditorProxy *proxy, OH_TextEditorProxy_GetTextIndexAtCursorFunc *getTextIndexAtCursorFunc)
```

**描述**

从[InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md)中获取[OH\_TextEditorProxy\_GetTextIndexAtCursorFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_gettextindexatcursorfunc)函数。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md) \*proxy | 指向被读取的[InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md)实例的指针。 |
| [OH\_TextEditorProxy\_GetTextIndexAtCursorFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_gettextindexatcursorfunc) \*getTextIndexAtCursorFunc | 表示从proxy获取到的函数[OH\_TextEditorProxy\_GetTextIndexAtCursorFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_gettextindexatcursorfunc)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [InputMethod\_ErrorCode](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) | 返回一个特定的错误码。  [IME\_ERR\_OK](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 表示成功。  [IME\_ERR\_NULL\_POINTER](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 非预期的空指针。  具体错误码可以参考 [InputMethod\_ErrorCode](capi-inputmethod-types-capi-h.md#inputmethod_errorcode)。 |

### OH\_TextEditorProxy\_GetReceivePrivateCommandFunc()

PhonePC/2in1TabletTVWearable

```
1. InputMethod_ErrorCode OH_TextEditorProxy_GetReceivePrivateCommandFunc(InputMethod_TextEditorProxy *proxy, OH_TextEditorProxy_ReceivePrivateCommandFunc *receivePrivateCommandFunc)
```

**描述**

从[InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md)中获取[OH\_TextEditorProxy\_ReceivePrivateCommandFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_receiveprivatecommandfunc)函数。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md) \*proxy | 指向被读取的[InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md)实例的指针。 |
| [OH\_TextEditorProxy\_ReceivePrivateCommandFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_receiveprivatecommandfunc) \*receivePrivateCommandFunc | 表示从proxy获取到的函数[OH\_TextEditorProxy\_ReceivePrivateCommandFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_receiveprivatecommandfunc)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [InputMethod\_ErrorCode](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) | 返回一个特定的错误码。  [IME\_ERR\_OK](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 表示成功。  [IME\_ERR\_NULL\_POINTER](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 非预期的空指针。  具体错误码可以参考 [InputMethod\_ErrorCode](capi-inputmethod-types-capi-h.md#inputmethod_errorcode)。 |

### OH\_TextEditorProxy\_GetSetPreviewTextFunc()

PhonePC/2in1TabletTVWearable

```
1. InputMethod_ErrorCode OH_TextEditorProxy_GetSetPreviewTextFunc(InputMethod_TextEditorProxy *proxy, OH_TextEditorProxy_SetPreviewTextFunc *setPreviewTextFunc)
```

**描述**

从[InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md)中获取[OH\_TextEditorProxy\_SetPreviewTextFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_setpreviewtextfunc)函数。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md) \*proxy | 指向被读取的[InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md)实例的指针。 |
| [OH\_TextEditorProxy\_SetPreviewTextFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_setpreviewtextfunc) \*setPreviewTextFunc | 表示从proxy获取到的函数[OH\_TextEditorProxy\_SetPreviewTextFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_setpreviewtextfunc)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [InputMethod\_ErrorCode](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) | 返回一个特定的错误码。  [IME\_ERR\_OK](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 表示成功。  [IME\_ERR\_NULL\_POINTER](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 非预期的空指针。  具体错误码可以参考 [InputMethod\_ErrorCode](capi-inputmethod-types-capi-h.md#inputmethod_errorcode)。 |

### OH\_TextEditorProxy\_GetFinishTextPreviewFunc()

PhonePC/2in1TabletTVWearable

```
1. InputMethod_ErrorCode OH_TextEditorProxy_GetFinishTextPreviewFunc(InputMethod_TextEditorProxy *proxy, OH_TextEditorProxy_FinishTextPreviewFunc *finishTextPreviewFunc)
```

**描述**

从[InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md)中获取[OH\_TextEditorProxy\_FinishTextPreviewFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_finishtextpreviewfunc)函数。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md) \*proxy | 指向被读取的[InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md)实例的指针。 |
| [OH\_TextEditorProxy\_FinishTextPreviewFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_finishtextpreviewfunc) \*finishTextPreviewFunc | 表示从proxy获取到的函数[OH\_TextEditorProxy\_FinishTextPreviewFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_finishtextpreviewfunc)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [InputMethod\_ErrorCode](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) | 返回一个特定的错误码。  [IME\_ERR\_OK](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 表示成功。  [IME\_ERR\_NULL\_POINTER](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 非预期的空指针。  具体错误码可以参考 [InputMethod\_ErrorCode](capi-inputmethod-types-capi-h.md#inputmethod_errorcode)。 |

### OH\_TextEditorProxy\_SetCallbackInMainThread()

PhonePC/2in1TabletTVWearable

```
1. InputMethod_ErrorCode OH_TextEditorProxy_SetCallbackInMainThread(InputMethod_TextEditorProxy *proxy, bool isCallbackInMainThread)
```

**描述**

为InputMethod\_TextEditorProxy的回调函数配置执行线程（主线程/IPC线程）。本接口仅控制InputMethod\_TextEditorProxy中除[OH\_TextEditorProxy\_GetTextConfigFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_gettextconfigfunc)之外的所有回调函数。[OH\_TextEditorProxy\_GetTextConfigFunc](capi-inputmethod-text-editor-proxy-capi-h.md#oh_texteditorproxy_gettextconfigfunc)的执行线程由调用[OH\_InputMethodController\_Attach](capi-inputmethod-controller-capi-h.md#oh_inputmethodcontroller_attach)的线程决定，不受本接口影响，若需该回调也在主线程执行，需确保[OH\_InputMethodController\_Attach](capi-inputmethod-controller-capi-h.md#oh_inputmethodcontroller_attach)在主线程调用。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [InputMethod\_TextEditorProxy](capi-inputmethod-inputmethod-texteditorproxy.md) \*proxy | 指向目标InputMethod\_TextEditorProxy实例的指针。 |
| bool isCallbackInMainThread | 线程执行策略。- true：回调函数切换至主线程执行（用于避免多线程并发问题）。避免在回调内执行耗时操作，防止主线程阻塞。- false：回调函数在IPC线程执行（可能存在多线程并发情况）。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [InputMethod\_ErrorCode](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) | 执行结果。  [IME\_ERR\_OK](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 配置成功。  [IME\_ERR\_NULL\_POINTER](capi-inputmethod-types-capi-h.md#inputmethod_errorcode) - 当proxy为NULL时返回。 |
