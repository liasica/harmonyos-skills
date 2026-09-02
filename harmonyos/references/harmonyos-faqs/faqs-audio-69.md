---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-audio-69
title: 使用OHAudio录制Base64格式的音频
breadcrumb: FAQ > 媒体开发 > 音频和视频 > 音频（Audio） > 使用OHAudio录制Base64格式的音频
category: harmonyos-faqs
scraped_at: 2026-09-02T15:04:21+08:00
doc_updated_at: 2026-07-09
content_hash: sha256:33d0517d9cc04bfaeb27bb75b5174452a051545cc25cb0b1ac673d563ec0080c
---

## 问题现象

使用[AudioCapturer](../harmonyos-references/arkts-apis-audio-audiocapturer.md)或[OHAudio](../harmonyos-references/capi-ohaudio.md)录制得到的是PCM格式的音频数据，PCM是原始音频数据，不能像MP3、AAC、WAV等音频文件一样直接被普通播放器识别播放。业务侧如果需要通过网络传输、缓存或提交给服务端处理，可以将录制得到的PCM数据转换为Base64字符串。

## 背景知识

* [AudioCapturer](../harmonyos-references/arkts-apis-audio-audiocapturer.md)和[OHAudio](../harmonyos-references/capi-ohaudio.md)用于音频输入，仅采集PCM格式的原始音频数据，需要应用持续读取音频数据并自行处理。
* PCM数据没有文件头或容器信息，播放器无法直接识别其采样率、通道数、采样格式等参数，因此不能直接播放。
* 如果需要录制可直接播放的音频文件，建议使用[AVRecorder](../harmonyos-references/arkts-apis-media-avrecorder.md)录制封装后的音频文件；如果必须使用[OHAudio](../harmonyos-references/capi-ohaudio.md)，需要自行将PCM数据封装为WAV，或编码为AAC等格式后再播放。
* Base64不是音频编码格式，而是二进制数据的文本编码方式。将PCM转换为Base64后，数据本质仍然是PCM，只是便于网络传输、文本存储或提交给服务端处理。

## 解决方案

[OHAudio](../harmonyos-references/capi-ohaudio.md)提供音频录制C API，录制获取的是PCM原始音频数据。可以先使用[native\_audiocapturer.h](../harmonyos-references/capi-native-audiocapturer-h.md)采集PCM数据，再将PCM二进制数据转换为Base64字符串。下述示例同时提供两条验证链路：Native侧直接将PCM转换为Base64；ArkTS侧读取保存的.pcm文件后再次转换为Base64，用于对比验证转换结果。

**说明** 

* 使用麦克风录音前，需要申请ohos.permission.MICROPHONE权限，申请方式参考[向用户申请授权](../harmonyos-guides/request-user-authorization.md)。
* 示例输出的是PCM数据对应的Base64字符串。如需生成WAV、AAC等格式的Base64字符串，需要先按目标音频格式封装或编码后，再进行Base64编码。
* 长时间录音时，不建议一直在内存中累积录音数据。可以分片上传，或先写入文件后再按需编码，避免内存占用过高。

1. 在module.json5中声明麦克风权限。

   ```json
   "requestPermissions": [
     {
       "name": "ohos.permission.MICROPHONE",
       "reason": "$string:reason",
       "usedScene": {
         "abilities": [
           "EntryAbility"
         ],
         "when": "inuse"
       }
     }
   ],
   ```
2. 在CMake脚本中链接NAPI和OHAudio动态库。

   target\_link\_libraries(entry PUBLIC libace\_napi.z.so libohaudio.so)。
3. 在Native侧创建[OH\_AudioCapturer](../harmonyos-references/capi-ohaudio-oh-audiocapturerstruct.md)实例，通过回调读取PCM数据。停止录音时，将同一份PCM数据写入.pcm文件，并转换为Base64字符串返回给ArkTS侧。

   ```
   #include "napi/native_api.h"

   #include <cstdint>
   #include <fstream>
   #include <mutex>
   #include <string>
   #include <vector>

   #include <ohaudio/native_audiocapturer.h>
   #include <ohaudio/native_audiostreambuilder.h>

   namespace {
   OH_AudioCapturer* g_audioCapturer = nullptr;
   std::vector<uint8_t> g_pcmData;
   std::mutex g_audioMutex;
   std::mutex g_pcmMutex;

   std::string EncodeBase64(const uint8_t* data, size_t len)
   {
       static constexpr char BASE64_TABLE[] =
           "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/";
       std::string result;
       result.reserve(((len + 2) / 3) * 4);

       for (size_t i = 0; i < len; i += 3) {
           uint32_t value = static_cast<uint32_t>(data[i]) << 16;
           if (i + 1 < len) {
               value |= static_cast<uint32_t>(data[i + 1]) << 8;
           }
           if (i + 2 < len) {
               value |= static_cast<uint32_t>(data[i + 2]);
           }

           result.push_back(BASE64_TABLE[(value >> 18) & 0x3F]);
           result.push_back(BASE64_TABLE[(value >> 12) & 0x3F]);
           result.push_back((i + 1 < len) ? BASE64_TABLE[(value >> 6) & 0x3F] : '=');
           result.push_back((i + 2 < len) ? BASE64_TABLE[value & 0x3F] : '=');
       }
       return result;
   }

   bool VerifyBase64Encoder()
   {
       struct Case {
           const uint8_t* data;
           size_t len;
           const char* expected;
       };

       static const uint8_t oneByte[] = {'M'};
       static const uint8_t twoBytes[] = {'M', 'a'};
       static const uint8_t threeBytes[] = {'M', 'a', 'n'};
       static const uint8_t binary[] = {0x00, 0x01, 0x02, 0x03};
       const Case cases[] = {
           {nullptr, 0, ""},
           {oneByte, sizeof(oneByte), "TQ=="},
           {twoBytes, sizeof(twoBytes), "TWE="},
           {threeBytes, sizeof(threeBytes), "TWFu"},
           {binary, sizeof(binary), "AAECAw=="},
       };

       for (const auto& item : cases) {
           if (EncodeBase64(item.data, item.len) != item.expected) {
               return false;
           }
       }
       return true;
   }

   void OnReadData(OH_AudioCapturer* capturer, void* userData, void* audioData, int32_t audioDataSize)
   {
       (void)capturer;
       (void)userData;

       if (audioData == nullptr || audioDataSize <= 0) {
           return;
       }

       auto* begin = static_cast<uint8_t*>(audioData);
       std::lock_guard<std::mutex> lock(g_pcmMutex);
       g_pcmData.insert(g_pcmData.end(), begin, begin + audioDataSize);
   }

   bool ConfigureCapturerBuilder(OH_AudioStreamBuilder* builder)
   {
       return OH_AudioStreamBuilder_SetSamplingRate(builder, 48000) == AUDIOSTREAM_SUCCESS &&
           OH_AudioStreamBuilder_SetChannelCount(builder, 1) == AUDIOSTREAM_SUCCESS &&
           OH_AudioStreamBuilder_SetSampleFormat(builder, AUDIOSTREAM_SAMPLE_S16LE) == AUDIOSTREAM_SUCCESS &&
           OH_AudioStreamBuilder_SetEncodingType(builder, AUDIOSTREAM_ENCODING_TYPE_RAW) == AUDIOSTREAM_SUCCESS &&
           OH_AudioStreamBuilder_SetCapturerInfo(builder, AUDIOSTREAM_SOURCE_TYPE_MIC) == AUDIOSTREAM_SUCCESS &&
           OH_AudioStreamBuilder_SetCapturerReadDataCallback(builder, OnReadData, nullptr) == AUDIOSTREAM_SUCCESS;
   }

   bool CreateCapturer()
   {
       OH_AudioStreamBuilder* builder = nullptr;
       if (OH_AudioStreamBuilder_Create(&builder, AUDIOSTREAM_TYPE_CAPTURER) != AUDIOSTREAM_SUCCESS || builder == nullptr) {
           return false;
       }

       if (!ConfigureCapturerBuilder(builder)) {
           OH_AudioStreamBuilder_Destroy(builder);
           return false;
       }

       OH_AudioCapturer* capturer = nullptr;
       OH_AudioStream_Result result = OH_AudioStreamBuilder_GenerateCapturer(builder, &capturer);
       OH_AudioStreamBuilder_Destroy(builder);
       if (result != AUDIOSTREAM_SUCCESS || capturer == nullptr) {
           return false;
       }

       g_audioCapturer = capturer;
       return true;
   }

   bool StartRecordInternal()
   {
       if (!VerifyBase64Encoder()) {
           return false;
       }

       std::lock_guard<std::mutex> audioLock(g_audioMutex);
       if (g_audioCapturer != nullptr) {
           return false;
       }

       if (!CreateCapturer()) {
           return false;
       }

       {
           std::lock_guard<std::mutex> pcmLock(g_pcmMutex);
           g_pcmData.clear();
       }

       if (OH_AudioCapturer_Start(g_audioCapturer) != AUDIOSTREAM_SUCCESS) {
           OH_AudioCapturer_Release(g_audioCapturer);
           g_audioCapturer = nullptr;
           return false;
       }
       return true;
   }

   std::vector<uint8_t> StopRecordAndGetPcmData()
   {
       OH_AudioCapturer* capturer = nullptr;
       {
           std::lock_guard<std::mutex> audioLock(g_audioMutex);
           capturer = g_audioCapturer;
           g_audioCapturer = nullptr;
       }

       if (capturer == nullptr) {
           return {};
       }

       OH_AudioCapturer_Stop(capturer);
       OH_AudioCapturer_Release(capturer);

       std::vector<uint8_t> pcmData;
       {
           std::lock_guard<std::mutex> pcmLock(g_pcmMutex);
           pcmData.swap(g_pcmData);
       }
       return pcmData;
   }

   bool WritePcmFile(const std::string& filePath, const std::vector<uint8_t>& pcmData)
   {
       if (filePath.empty() || pcmData.empty()) {
           return false;
       }

       std::ofstream output(filePath, std::ios::binary | std::ios::trunc);
       if (!output.is_open()) {
           return false;
       }

       output.write(reinterpret_cast<const char*>(pcmData.data()), static_cast<std::streamsize>(pcmData.size()));
       return output.good();
   }

   bool GetStringArgument(napi_env env, napi_callback_info info, std::string& value)
   {
       size_t argc = 1;
       napi_value args[1] = {nullptr};
       napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);
       if (argc < 1 || args[0] == nullptr) {
           return false;
       }

       size_t length = 0;
       if (napi_get_value_string_utf8(env, args[0], nullptr, 0, &length) != napi_ok) {
           return false;
       }

       std::vector<char> buffer(length + 1);
       if (napi_get_value_string_utf8(env, args[0], buffer.data(), buffer.size(), &length) != napi_ok) {
           return false;
       }

       value.assign(buffer.data(), length);
       return true;
   }
   } // namespace

   static napi_value StartRecord(napi_env env, napi_callback_info info)
   {
       (void)info;

       napi_value result;
       napi_get_boolean(env, StartRecordInternal(), &result);
       return result;
   }

   static napi_value StopRecordToFile(napi_env env, napi_callback_info info)
   {
       std::string filePath;
       if (!GetStringArgument(env, info, filePath)) {
           napi_value empty;
           napi_create_string_utf8(env, "", NAPI_AUTO_LENGTH, &empty);
           return empty;
       }

       std::vector<uint8_t> pcmData = StopRecordAndGetPcmData();
       if (!WritePcmFile(filePath, pcmData)) {
           napi_value empty;
           napi_create_string_utf8(env, "", NAPI_AUTO_LENGTH, &empty);
           return empty;
       }

       std::string base64 = EncodeBase64(pcmData.data(), pcmData.size());
       napi_value result;
       napi_create_string_utf8(env, base64.c_str(), base64.size(), &result);
       return result;
   }

   EXTERN_C_START
   static napi_value Init(napi_env env, napi_value exports)
   {
       napi_property_descriptor desc[] = {
           { "startRecord", nullptr, StartRecord, nullptr, nullptr, nullptr, napi_default, nullptr },
           { "stopRecordToFile", nullptr, StopRecordToFile, nullptr, nullptr, nullptr, napi_default, nullptr },
       };
       napi_define_properties(env, exports, sizeof(desc) / sizeof(desc[0]), desc);
       return exports;
   }
   EXTERN_C_END

   static napi_module audioRecorderModule = {
       .nm_version = 1,
       .nm_flags = 0,
       .nm_filename = nullptr,
       .nm_register_func = Init,
       .nm_modname = "entry",
       .nm_priv = nullptr,
       .reserved = { 0 },
   };

   extern "C" __attribute__((constructor)) void RegisterAudioRecorderModule(void)
   {
       napi_module_register(&audioRecorderModule);
   }
   ```
4. Index.d.ts中C接口申明。

   ```ts
   export const startRecord: () => boolean;
   export const stopRecordToFile: (path: string) => string;
   ```
5. 在Index.ets中申请麦克风权限，控制录音，并提供两种Base64输出方式：一种是Native侧停止录音时直接返回Base64，另一种是ArkTS侧读取.pcm文件后重新转换为Base64。

   ```ts
   import audioRecorder from 'libentry.so';
   import { abilityAccessCtrl, common, Permissions } from '@kit.AbilityKit';
   import { BusinessError } from '@kit.BasicServicesKit';
   import { fileIo } from '@kit.CoreFileKit';

   const MICROPHONE_PERMISSION: Permissions = 'ohos.permission.MICROPHONE';
   const BASE64_CHARS: string = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/';

   class PcmToBase64 {
     private context: common.UIAbilityContext

     constructor(context: common.UIAbilityContext) {
       this.context = context
     }

     private encodeBytes(bytes: Uint8Array, validLength: number): string {
       let result: string = ""
       for (let i = 0; i < validLength; i += 3) {
         const first: number = bytes[i]
         const second: number = i + 1 < validLength ? bytes[i + 1] : 0
         const third: number = i + 2 < validLength ? bytes[i + 2] : 0
         const value: number = (first << 16) | (second << 8) | third

         result += BASE64_CHARS.charAt((value >> 18) & 0x3F)
         result += BASE64_CHARS.charAt((value >> 12) & 0x3F)
         result += i + 1 < validLength ? BASE64_CHARS.charAt((value >> 6) & 0x3F) : '='
         result += i + 2 < validLength ? BASE64_CHARS.charAt(value & 0x3F) : '='
       }
       return result
     }

     pcmTranslate(pcmFilePath: string): string {
       let inputFile: fileIo.File | undefined = undefined
       let outputFile: fileIo.File | undefined = undefined
       const outputPath: string = `${this.context.filesDir}/pcm_base64_${Date.now()}.txt`

       try {
         inputFile = fileIo.openSync(pcmFilePath, fileIo.OpenMode.READ_ONLY)
         outputFile = fileIo.openSync(outputPath, fileIo.OpenMode.CREATE | fileIo.OpenMode.TRUNC | fileIo.OpenMode.WRITE_ONLY)

         let pending: number[] = []
         let buffer: ArrayBuffer = new ArrayBuffer(1024 * 256)
         let readSize: number = 0
         do {
           readSize = fileIo.readSync(inputFile.fd, buffer)
           if (readSize <= 0) {
             break
           }

           let chunk: Uint8Array = new Uint8Array(buffer, 0, readSize)
           if (pending.length > 0) {
             let merged: Uint8Array = new Uint8Array(pending.length + readSize)
             for (let i = 0; i < pending.length; i++) {
               merged[i] = pending[i]
             }
             merged.set(chunk, pending.length)
             chunk = merged
           }

           const encodeLength: number = Math.floor(chunk.length / 3) * 3
           if (encodeLength > 0) {
             fileIo.writeSync(outputFile.fd, this.encodeBytes(chunk, encodeLength))
           }

           pending = []
           for (let i = encodeLength; i < chunk.length; i++) {
             pending.push(chunk[i])
           }
         } while (readSize > 0)

         if (pending.length > 0) {
           fileIo.writeSync(outputFile.fd, this.encodeBytes(new Uint8Array(pending), pending.length))
         }
         return outputPath
       } catch (error) {
         console.error(`PCM to Base64 failed: ${JSON.stringify(error)}`)
         return ""
       } finally {
         if (inputFile !== undefined) {
           fileIo.closeSync(inputFile)
         }
         if (outputFile !== undefined) {
           fileIo.closeSync(outputFile)
         }
       }
     }
   }

   @Entry
   @Component
   struct Index {
     @State status: string = "Ready"
     @State recordTime: number = 0
     @State base64Length: number = 0
     @State base64Preview: string = ""
     @State pcmPath: string = ""
     @State savePath: string = ""
     @State pcmByteLength: number = 0
     @State canSaveBase64: boolean = false
     private base64Data: string = ""
     private timerId: number = -1

     private buildBase64Preview(base64: string): string {
       if (base64.length <= 180) {
         return base64
       }
       const head: string = base64.substring(0, 60)
       const middleStart: number = Math.max(0, Math.floor(base64.length / 2) - 30)
       const middle: string = base64.substring(middleStart, middleStart + 60)
       const tail: string = base64.substring(base64.length - 60)
       return `${head}\n...\n${middle}\n...\n${tail}`
     }

     private clearRecordData(): void {
       this.recordTime = 0
       this.base64Length = 0
       this.base64Preview = ""
       this.pcmPath = ""
       this.savePath = ""
       this.pcmByteLength = 0
       this.canSaveBase64 = false
       this.base64Data = ""
     }

     private getAbilityContext(): common.UIAbilityContext {
       return this.getUIContext().getHostContext() as common.UIAbilityContext
     }

     private async requestMicrophonePermission(): Promise<boolean> {
       try {
         const context = this.getAbilityContext()
         const atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager()
         const result = await atManager.requestPermissionsFromUser(context, [MICROPHONE_PERMISSION])
         return result.authResults.length > 0 &&
           result.authResults[0] === abilityAccessCtrl.GrantStatus.PERMISSION_GRANTED
       } catch (error) {
         const err = error as BusinessError
         console.error(`Request microphone permission failed, code: ${err.code}, message: ${err.message}`)
         return false
       }
     }

     private async startRecord(): Promise<void> {
       const granted: boolean = await this.requestMicrophonePermission()
       if (!granted) {
         this.status = "Mic Permission Denied"
         return
       }

       let result: boolean = audioRecorder.startRecord()
       if (result) {
         this.status = "Recording"
         this.clearRecordData()
         this.timerId = setInterval(() => {
           this.recordTime++
         }, 1000) as number
       } else {
         this.status = "Start Failed"
       }
     }

     private saveBase64ToFile(): void {
       if (this.base64Data.length === 0) {
         this.status = "No Base64 Data"
         return
       }

       const context = this.getAbilityContext()
       let filePath: string = `${context.filesDir}/audio_base64_${Date.now()}.txt`
       let file: fileIo.File | undefined = undefined
       try {
         file = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE | fileIo.OpenMode.TRUNC)
         fileIo.writeSync(file.fd, this.base64Data)
         this.savePath = filePath
         this.status = "Saved"
       } catch (error) {
         this.status = "Save Failed"
         console.error(`Save Base64 failed: ${JSON.stringify(error)}`)
       } finally {
         if (file !== undefined) {
           fileIo.closeSync(file)
         }
       }
     }

     private pcmToBase64(): void {
       if (this.pcmPath.length === 0) {
         this.status = "No PCM File"
         return
       }

       const translator = new PcmToBase64(this.getAbilityContext())
       const outputPath: string = translator.pcmTranslate(this.pcmPath)
       if (outputPath.length === 0) {
         this.status = "PCM To Base64 Failed"
         return
       }

       this.savePath = outputPath
       this.status = "PCM Base64 Saved"
     }

     build() {
       Scroll() {
         Column() {
           Text("Audio Recorder Test")
             .fontSize(28)
             .fontWeight(FontWeight.Bold)
             .margin({ bottom: 20 })

           Text(`Status: ${this.status}`).fontSize(18).margin({ bottom: 12 })
           Text(`Duration: ${this.recordTime} s`).fontSize(18).margin({ bottom: 12 })
           Text(`Base64 Length: ${this.base64Length} chars`).fontSize(18).margin({ bottom: 12 })
           Text(`PCM Bytes: ${this.pcmByteLength}`).fontSize(18).margin({ bottom: 20 })

           if (this.base64Preview.length > 0) {
             Text(this.base64Preview)
               .fontSize(12)
               .maxLines(3)
               .textOverflow({ overflow: TextOverflow.Ellipsis })
               .backgroundColor("#F5F5F5")
               .padding(10)
               .width('100%')
               .margin({ bottom: 12 })
           }

           if (this.pcmPath.length > 0) {
             Text(`PCM File: ${this.pcmPath}`)
               .fontSize(12)
               .maxLines(3)
               .textOverflow({ overflow: TextOverflow.Ellipsis })
               .backgroundColor("#F5F5F5")
               .padding(10)
               .width('100%')
               .margin({ bottom: 12 })
           }

           if (this.savePath.length > 0) {
             Text(`Saved File: ${this.savePath}`)
               .fontSize(12)
               .maxLines(3)
               .textOverflow({ overflow: TextOverflow.Ellipsis })
               .backgroundColor("#F5F5F5")
               .padding(10)
               .width('100%')
               .margin({ bottom: 12 })
           }

           Row({ space: 20 }) {
             Button("Start Record")
               .width(140)
               .height(50)
               .enabled(this.status !== "Recording")
               .onClick(async () => {
                 await this.startRecord()
               })

             Button("Stop Record")
               .width(140)
               .height(50)
               .enabled(this.status === "Recording")
               .onClick(() => {
                 if (this.timerId != -1) {
                   clearInterval(this.timerId)
                   this.timerId = -1
                 }

                 const context = this.getAbilityContext()
                 const pcmPath: string = `${context.filesDir}/audio_${Date.now()}.pcm`
                 let base64: string = audioRecorder.stopRecordToFile(pcmPath)
                 this.pcmPath = base64.length > 0 ? pcmPath : ""
                 this.base64Data = base64
                 this.base64Length = base64.length
                 this.base64Preview = this.buildBase64Preview(base64)
                 this.canSaveBase64 = base64.length > 0
                 this.pcmByteLength = base64.length > 0 ? fileIo.statSync(pcmPath).size : 0
                 this.status = base64.length > 0 ? "Stopped" : "No Audio Data"
               })
           }
           .margin({ bottom: 20 })

           Row({ space: 20 }) {
             Button("Save Base64")
               .width(140)
               .enabled(this.canSaveBase64)
               .onClick(() => {
                 this.saveBase64ToFile()
               })

             Button("PCM To Base64")
               .width(140)
               .enabled(this.pcmPath.length > 0)
               .onClick(() => {
                 this.pcmToBase64()
               })
           }
           .margin({ bottom: 15 })

           Button("Clear")
             .width(120)
             .onClick(() => {
               this.status = "Ready"
               this.clearRecordData()
             })
         }
         .width('100%')
         .padding(20)
       }
       .width('100%')
       .height('100%')
     }

     aboutToDisappear() {
       if (this.status === "Recording") {
         audioRecorder.stopRecordToFile(`${this.getAbilityContext().filesDir}/audio_${Date.now()}.pcm`)
         if (this.timerId != -1) {
           clearInterval(this.timerId)
           this.timerId = -1
         }
       }
     }
   }
   ```
6. 验证PCM转Base64结果。停止录音后会生成.pcm文件，并得到Native侧直接转换出的Base64。点击PCM To Base64后，ArkTS侧会读取同一个.pcm文件并输出新的Base64文本文件。可以将两个Base64文件拉取到电脑后比较，若两个文件完全一致，且Base64解码后的二进制内容与原.pcm文件一致，则说明转换结果正确。

   hdc file recv /data/app/el2/100/base/<bundleName>/haps/entry/files/audio\_base64\_xxx.txt .

   hdc file recv /data/app/el2/100/base/<bundleName>/haps/entry/files/pcm\_base64\_xxx.txt .

   hdc file recv /data/app/el2/100/base/<bundleName>/haps/entry/files/audio\_xxx.pcm .

   cmp audio\_base64\_xxx.txt pcm\_base64\_xxx.txt

   base64 -D -i pcm\_base64\_xxx.txt -o decoded.pcm

   cmp audio\_xxx.pcm decoded.pcm
7. 如果服务端需要识别音频参数，需要同时约定采样率、通道数、采样格式和编码类型。

   上述示例对应的音频参数如下：

   | 参数 | 取值 |
   | --- | --- |
   | 采样率 | 48000 Hz |
   | 通道数 | 单声道 |
   | 采样格式 | S16LE |
   | 编码类型 | PCM RAW |
