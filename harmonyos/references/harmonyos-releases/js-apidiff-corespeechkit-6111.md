---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-corespeechkit-6111
title: Core Speech Kit
breadcrumb: 版本说明 > 更多版本 > 6.1.1(24) > OS平台能力 > API变更清单 > 6.1.1(24) Beta1引入的API > Core Speech Kit
category: harmonyos-releases
scraped_at: 2026-09-02T14:49:07+08:00
doc_updated_at: 2026-06-27
content_hash: sha256:84bc3851fe5b4f1519257d9bbe235681681fb624de4c8882ba2c7d80abce80e5
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| API从不支持元服务到支持元服务 | 类名：global；  API声明：declare namespace textToSpeech  差异内容：NA | 类名：global；  API声明：declare namespace textToSpeech  差异内容：atomicservice | api/@hms.ai.textToSpeech.d.ts |
| API从不支持元服务到支持元服务 | 类名：textToSpeech；  API声明：function createEngine(createEngineParams: CreateEngineParams, callback: AsyncCallback<TextToSpeechEngine>): void;  差异内容：NA | 类名：textToSpeech；  API声明：function createEngine(createEngineParams: CreateEngineParams, callback: AsyncCallback<TextToSpeechEngine>): void;  差异内容：atomicservice | api/@hms.ai.textToSpeech.d.ts |
| API从不支持元服务到支持元服务 | 类名：textToSpeech；  API声明：function createEngine(createEngineParams: CreateEngineParams): Promise<TextToSpeechEngine>;  差异内容：NA | 类名：textToSpeech；  API声明：function createEngine(createEngineParams: CreateEngineParams): Promise<TextToSpeechEngine>;  差异内容：atomicservice | api/@hms.ai.textToSpeech.d.ts |
| API从不支持元服务到支持元服务 | 类名：textToSpeech；  API声明：export interface TextToSpeechEngine  差异内容：NA | 类名：textToSpeech；  API声明：export interface TextToSpeechEngine  差异内容：atomicservice | api/@hms.ai.textToSpeech.d.ts |
| API从不支持元服务到支持元服务 | 类名：TextToSpeechEngine；  API声明：setListener(listener: SpeakListener): void;  差异内容：NA | 类名：TextToSpeechEngine；  API声明：setListener(listener: SpeakListener): void;  差异内容：atomicservice | api/@hms.ai.textToSpeech.d.ts |
| API从不支持元服务到支持元服务 | 类名：TextToSpeechEngine；  API声明：speak(text: string, speakParams: SpeakParams): void;  差异内容：NA | 类名：TextToSpeechEngine；  API声明：speak(text: string, speakParams: SpeakParams): void;  差异内容：atomicservice | api/@hms.ai.textToSpeech.d.ts |
| API从不支持元服务到支持元服务 | 类名：TextToSpeechEngine；  API声明：listVoices(params: VoiceQuery, callback: AsyncCallback<Array<VoiceInfo>>): void;  差异内容：NA | 类名：TextToSpeechEngine；  API声明：listVoices(params: VoiceQuery, callback: AsyncCallback<Array<VoiceInfo>>): void;  差异内容：atomicservice | api/@hms.ai.textToSpeech.d.ts |
| API从不支持元服务到支持元服务 | 类名：TextToSpeechEngine；  API声明：listVoices(params: VoiceQuery): Promise<Array<VoiceInfo>>;  差异内容：NA | 类名：TextToSpeechEngine；  API声明：listVoices(params: VoiceQuery): Promise<Array<VoiceInfo>>;  差异内容：atomicservice | api/@hms.ai.textToSpeech.d.ts |
| API从不支持元服务到支持元服务 | 类名：TextToSpeechEngine；  API声明：stop(): void;  差异内容：NA | 类名：TextToSpeechEngine；  API声明：stop(): void;  差异内容：atomicservice | api/@hms.ai.textToSpeech.d.ts |
| API从不支持元服务到支持元服务 | 类名：TextToSpeechEngine；  API声明：isBusy(): boolean;  差异内容：NA | 类名：TextToSpeechEngine；  API声明：isBusy(): boolean;  差异内容：atomicservice | api/@hms.ai.textToSpeech.d.ts |
| API从不支持元服务到支持元服务 | 类名：TextToSpeechEngine；  API声明：shutdown(): void;  差异内容：NA | 类名：TextToSpeechEngine；  API声明：shutdown(): void;  差异内容：atomicservice | api/@hms.ai.textToSpeech.d.ts |
| API从不支持元服务到支持元服务 | 类名：textToSpeech；  API声明：export interface SpeakListener  差异内容：NA | 类名：textToSpeech；  API声明：export interface SpeakListener  差异内容：atomicservice | api/@hms.ai.textToSpeech.d.ts |
| API从不支持元服务到支持元服务 | 类名：SpeakListener；  API声明：onStart(requestId: string, response: StartResponse): void;  差异内容：NA | 类名：SpeakListener；  API声明：onStart(requestId: string, response: StartResponse): void;  差异内容：atomicservice | api/@hms.ai.textToSpeech.d.ts |
| API从不支持元服务到支持元服务 | 类名：SpeakListener；  API声明：onComplete(requestId: string, response: CompleteResponse): void;  差异内容：NA | 类名：SpeakListener；  API声明：onComplete(requestId: string, response: CompleteResponse): void;  差异内容：atomicservice | api/@hms.ai.textToSpeech.d.ts |
| API从不支持元服务到支持元服务 | 类名：SpeakListener；  API声明：onStop(requestId: string, response: StopResponse): void;  差异内容：NA | 类名：SpeakListener；  API声明：onStop(requestId: string, response: StopResponse): void;  差异内容：atomicservice | api/@hms.ai.textToSpeech.d.ts |
| API从不支持元服务到支持元服务 | 类名：SpeakListener；  API声明：onError(requestId: string, errorCode: number, errorMessage: string): void;  差异内容：NA | 类名：SpeakListener；  API声明：onError(requestId: string, errorCode: number, errorMessage: string): void;  差异内容：atomicservice | api/@hms.ai.textToSpeech.d.ts |
| API从不支持元服务到支持元服务 | 类名：SpeakListener；  API声明：onData?: OnDataCallback;  差异内容：NA | 类名：SpeakListener；  API声明：onData?: OnDataCallback;  差异内容：atomicservice | api/@hms.ai.textToSpeech.d.ts |
| API从不支持元服务到支持元服务 | 类名：textToSpeech；  API声明：export interface CreateEngineParams  差异内容：NA | 类名：textToSpeech；  API声明：export interface CreateEngineParams  差异内容：atomicservice | api/@hms.ai.textToSpeech.d.ts |
| API从不支持元服务到支持元服务 | 类名：CreateEngineParams；  API声明：language: string;  差异内容：NA | 类名：CreateEngineParams；  API声明：language: string;  差异内容：atomicservice | api/@hms.ai.textToSpeech.d.ts |
| API从不支持元服务到支持元服务 | 类名：CreateEngineParams；  API声明：person: number;  差异内容：NA | 类名：CreateEngineParams；  API声明：person: number;  差异内容：atomicservice | api/@hms.ai.textToSpeech.d.ts |
| API从不支持元服务到支持元服务 | 类名：CreateEngineParams；  API声明：online: number;  差异内容：NA | 类名：CreateEngineParams；  API声明：online: number;  差异内容：atomicservice | api/@hms.ai.textToSpeech.d.ts |
| API从不支持元服务到支持元服务 | 类名：CreateEngineParams；  API声明：extraParams?: Record<string, Object>;  差异内容：NA | 类名：CreateEngineParams；  API声明：extraParams?: Record<string, Object>;  差异内容：atomicservice | api/@hms.ai.textToSpeech.d.ts |
| API从不支持元服务到支持元服务 | 类名：textToSpeech；  API声明：export interface SpeakParams  差异内容：NA | 类名：textToSpeech；  API声明：export interface SpeakParams  差异内容：atomicservice | api/@hms.ai.textToSpeech.d.ts |
| API从不支持元服务到支持元服务 | 类名：SpeakParams；  API声明：requestId: string;  差异内容：NA | 类名：SpeakParams；  API声明：requestId: string;  差异内容：atomicservice | api/@hms.ai.textToSpeech.d.ts |
| API从不支持元服务到支持元服务 | 类名：SpeakParams；  API声明：extraParams?: Record<string, Object>;  差异内容：NA | 类名：SpeakParams；  API声明：extraParams?: Record<string, Object>;  差异内容：atomicservice | api/@hms.ai.textToSpeech.d.ts |
| API从不支持元服务到支持元服务 | 类名：textToSpeech；  API声明：export interface VoiceQuery  差异内容：NA | 类名：textToSpeech；  API声明：export interface VoiceQuery  差异内容：atomicservice | api/@hms.ai.textToSpeech.d.ts |
| API从不支持元服务到支持元服务 | 类名：VoiceQuery；  API声明：requestId: string;  差异内容：NA | 类名：VoiceQuery；  API声明：requestId: string;  差异内容：atomicservice | api/@hms.ai.textToSpeech.d.ts |
| API从不支持元服务到支持元服务 | 类名：VoiceQuery；  API声明：online: number;  差异内容：NA | 类名：VoiceQuery；  API声明：online: number;  差异内容：atomicservice | api/@hms.ai.textToSpeech.d.ts |
| API从不支持元服务到支持元服务 | 类名：VoiceQuery；  API声明：extraParams?: Record<string, Object>;  差异内容：NA | 类名：VoiceQuery；  API声明：extraParams?: Record<string, Object>;  差异内容：atomicservice | api/@hms.ai.textToSpeech.d.ts |
| API从不支持元服务到支持元服务 | 类名：textToSpeech；  API声明：export interface VoiceInfo  差异内容：NA | 类名：textToSpeech；  API声明：export interface VoiceInfo  差异内容：atomicservice | api/@hms.ai.textToSpeech.d.ts |
| API从不支持元服务到支持元服务 | 类名：VoiceInfo；  API声明：language: string;  差异内容：NA | 类名：VoiceInfo；  API声明：language: string;  差异内容：atomicservice | api/@hms.ai.textToSpeech.d.ts |
| API从不支持元服务到支持元服务 | 类名：VoiceInfo；  API声明：person: number;  差异内容：NA | 类名：VoiceInfo；  API声明：person: number;  差异内容：atomicservice | api/@hms.ai.textToSpeech.d.ts |
| API从不支持元服务到支持元服务 | 类名：VoiceInfo；  API声明：style: string;  差异内容：NA | 类名：VoiceInfo；  API声明：style: string;  差异内容：atomicservice | api/@hms.ai.textToSpeech.d.ts |
| API从不支持元服务到支持元服务 | 类名：VoiceInfo；  API声明：gender: string;  差异内容：NA | 类名：VoiceInfo；  API声明：gender: string;  差异内容：atomicservice | api/@hms.ai.textToSpeech.d.ts |
| API从不支持元服务到支持元服务 | 类名：VoiceInfo；  API声明：description: string;  差异内容：NA | 类名：VoiceInfo；  API声明：description: string;  差异内容：atomicservice | api/@hms.ai.textToSpeech.d.ts |
| API从不支持元服务到支持元服务 | 类名：VoiceInfo；  API声明：status?: string;  差异内容：NA | 类名：VoiceInfo；  API声明：status?: string;  差异内容：atomicservice | api/@hms.ai.textToSpeech.d.ts |
| API从不支持元服务到支持元服务 | 类名：textToSpeech；  API声明：export interface StartResponse  差异内容：NA | 类名：textToSpeech；  API声明：export interface StartResponse  差异内容：atomicservice | api/@hms.ai.textToSpeech.d.ts |
| API从不支持元服务到支持元服务 | 类名：StartResponse；  API声明：audioType: string;  差异内容：NA | 类名：StartResponse；  API声明：audioType: string;  差异内容：atomicservice | api/@hms.ai.textToSpeech.d.ts |
| API从不支持元服务到支持元服务 | 类名：StartResponse；  API声明：sampleRate: number;  差异内容：NA | 类名：StartResponse；  API声明：sampleRate: number;  差异内容：atomicservice | api/@hms.ai.textToSpeech.d.ts |
| API从不支持元服务到支持元服务 | 类名：StartResponse；  API声明：sampleBit: number;  差异内容：NA | 类名：StartResponse；  API声明：sampleBit: number;  差异内容：atomicservice | api/@hms.ai.textToSpeech.d.ts |
| API从不支持元服务到支持元服务 | 类名：StartResponse；  API声明：audioChannel: number;  差异内容：NA | 类名：StartResponse；  API声明：audioChannel: number;  差异内容：atomicservice | api/@hms.ai.textToSpeech.d.ts |
| API从不支持元服务到支持元服务 | 类名：StartResponse；  API声明：compressRate: number;  差异内容：NA | 类名：StartResponse；  API声明：compressRate: number;  差异内容：atomicservice | api/@hms.ai.textToSpeech.d.ts |
| API从不支持元服务到支持元服务 | 类名：textToSpeech；  API声明：export interface StopResponse  差异内容：NA | 类名：textToSpeech；  API声明：export interface StopResponse  差异内容：atomicservice | api/@hms.ai.textToSpeech.d.ts |
| API从不支持元服务到支持元服务 | 类名：StopResponse；  API声明：type: number;  差异内容：NA | 类名：StopResponse；  API声明：type: number;  差异内容：atomicservice | api/@hms.ai.textToSpeech.d.ts |
| API从不支持元服务到支持元服务 | 类名：StopResponse；  API声明：message: string;  差异内容：NA | 类名：StopResponse；  API声明：message: string;  差异内容：atomicservice | api/@hms.ai.textToSpeech.d.ts |
| API从不支持元服务到支持元服务 | 类名：textToSpeech；  API声明：export interface CompleteResponse  差异内容：NA | 类名：textToSpeech；  API声明：export interface CompleteResponse  差异内容：atomicservice | api/@hms.ai.textToSpeech.d.ts |
| API从不支持元服务到支持元服务 | 类名：CompleteResponse；  API声明：type: number;  差异内容：NA | 类名：CompleteResponse；  API声明：type: number;  差异内容：atomicservice | api/@hms.ai.textToSpeech.d.ts |
| API从不支持元服务到支持元服务 | 类名：CompleteResponse；  API声明：message: string;  差异内容：NA | 类名：CompleteResponse；  API声明：message: string;  差异内容：atomicservice | api/@hms.ai.textToSpeech.d.ts |
| API从不支持元服务到支持元服务 | 类名：textToSpeech；  API声明：export interface SynthesisResponse  差异内容：NA | 类名：textToSpeech；  API声明：export interface SynthesisResponse  差异内容：atomicservice | api/@hms.ai.textToSpeech.d.ts |
| API从不支持元服务到支持元服务 | 类名：SynthesisResponse；  API声明：sequence: number;  差异内容：NA | 类名：SynthesisResponse；  API声明：sequence: number;  差异内容：atomicservice | api/@hms.ai.textToSpeech.d.ts |
| API从不支持元服务到支持元服务 | 类名：SynthesisResponse；  API声明：audioType: string;  差异内容：NA | 类名：SynthesisResponse；  API声明：audioType: string;  差异内容：atomicservice | api/@hms.ai.textToSpeech.d.ts |
| API从不支持元服务到支持元服务 | 类名：textToSpeech；  API声明：function listVoices(queryParams: VoiceQuery): Promise<VoiceInfo[]>;  差异内容：NA | 类名：textToSpeech；  API声明：function listVoices(queryParams: VoiceQuery): Promise<VoiceInfo[]>;  差异内容：atomicservice | api/@hms.ai.textToSpeech.d.ts |
| API从不支持元服务到支持元服务 | 类名：textToSpeech；  API声明：function downloadVoice(downloadParams: VoiceDownload, callback: AsyncCallback<DownloadResponse>): void;  差异内容：NA | 类名：textToSpeech；  API声明：function downloadVoice(downloadParams: VoiceDownload, callback: AsyncCallback<DownloadResponse>): void;  差异内容：atomicservice | api/@hms.ai.textToSpeech.d.ts |
| API从不支持元服务到支持元服务 | 类名：textToSpeech；  API声明：type OnDataCallback = (requestId: string, audio: ArrayBuffer, response: SynthesisResponse) => void;  差异内容：NA | 类名：textToSpeech；  API声明：type OnDataCallback = (requestId: string, audio: ArrayBuffer, response: SynthesisResponse) => void;  差异内容：atomicservice | api/@hms.ai.textToSpeech.d.ts |
| API从不支持元服务到支持元服务 | 类名：textToSpeech；  API声明：export interface VoiceDownload  差异内容：NA | 类名：textToSpeech；  API声明：export interface VoiceDownload  差异内容：atomicservice | api/@hms.ai.textToSpeech.d.ts |
| API从不支持元服务到支持元服务 | 类名：VoiceDownload；  API声明：requestId: string;  差异内容：NA | 类名：VoiceDownload；  API声明：requestId: string;  差异内容：atomicservice | api/@hms.ai.textToSpeech.d.ts |
| API从不支持元服务到支持元服务 | 类名：VoiceDownload；  API声明：language: string;  差异内容：NA | 类名：VoiceDownload；  API声明：language: string;  差异内容：atomicservice | api/@hms.ai.textToSpeech.d.ts |
| API从不支持元服务到支持元服务 | 类名：VoiceDownload；  API声明：person: number;  差异内容：NA | 类名：VoiceDownload；  API声明：person: number;  差异内容：atomicservice | api/@hms.ai.textToSpeech.d.ts |
| API从不支持元服务到支持元服务 | 类名：VoiceDownload；  API声明：style: string;  差异内容：NA | 类名：VoiceDownload；  API声明：style: string;  差异内容：atomicservice | api/@hms.ai.textToSpeech.d.ts |
| API从不支持元服务到支持元服务 | 类名：textToSpeech；  API声明：export interface DownloadResponse  差异内容：NA | 类名：textToSpeech；  API声明：export interface DownloadResponse  差异内容：atomicservice | api/@hms.ai.textToSpeech.d.ts |
| API从不支持元服务到支持元服务 | 类名：DownloadResponse；  API声明：requestId: string;  差异内容：NA | 类名：DownloadResponse；  API声明：requestId: string;  差异内容：atomicservice | api/@hms.ai.textToSpeech.d.ts |
| API从不支持元服务到支持元服务 | 类名：DownloadResponse；  API声明：on(type: 'start', callback: Callback<string>): void;  差异内容：NA | 类名：DownloadResponse；  API声明：on(type: 'start', callback: Callback<string>): void;  差异内容：atomicservice | api/@hms.ai.textToSpeech.d.ts |
| API从不支持元服务到支持元服务 | 类名：DownloadResponse；  API声明：off(type: 'start', callback?: Callback<string>): void;  差异内容：NA | 类名：DownloadResponse；  API声明：off(type: 'start', callback?: Callback<string>): void;  差异内容：atomicservice | api/@hms.ai.textToSpeech.d.ts |
| API从不支持元服务到支持元服务 | 类名：DownloadResponse；  API声明：on(type: 'progress', callback: Callback<string>): void;  差异内容：NA | 类名：DownloadResponse；  API声明：on(type: 'progress', callback: Callback<string>): void;  差异内容：atomicservice | api/@hms.ai.textToSpeech.d.ts |
| API从不支持元服务到支持元服务 | 类名：DownloadResponse；  API声明：off(type: 'progress', callback?: Callback<string>): void;  差异内容：NA | 类名：DownloadResponse；  API声明：off(type: 'progress', callback?: Callback<string>): void;  差异内容：atomicservice | api/@hms.ai.textToSpeech.d.ts |
| API从不支持元服务到支持元服务 | 类名：DownloadResponse；  API声明：on(type: 'complete', callback: Callback<VoiceInfo>): void;  差异内容：NA | 类名：DownloadResponse；  API声明：on(type: 'complete', callback: Callback<VoiceInfo>): void;  差异内容：atomicservice | api/@hms.ai.textToSpeech.d.ts |
| API从不支持元服务到支持元服务 | 类名：DownloadResponse；  API声明：off(type: 'complete', callback?: Callback<VoiceInfo>): void;  差异内容：NA | 类名：DownloadResponse；  API声明：off(type: 'complete', callback?: Callback<VoiceInfo>): void;  差异内容：atomicservice | api/@hms.ai.textToSpeech.d.ts |
| API从不支持元服务到支持元服务 | 类名：DownloadResponse；  API声明：on(type: 'cancel', callback: Callback<string>): void;  差异内容：NA | 类名：DownloadResponse；  API声明：on(type: 'cancel', callback: Callback<string>): void;  差异内容：atomicservice | api/@hms.ai.textToSpeech.d.ts |
| API从不支持元服务到支持元服务 | 类名：DownloadResponse；  API声明：off(type: 'cancel', callback?: Callback<string>): void;  差异内容：NA | 类名：DownloadResponse；  API声明：off(type: 'cancel', callback?: Callback<string>): void;  差异内容：atomicservice | api/@hms.ai.textToSpeech.d.ts |
| API从不支持元服务到支持元服务 | 类名：DownloadResponse；  API声明：on(type: 'error', callback: ErrorCallback<BusinessError>): void;  差异内容：NA | 类名：DownloadResponse；  API声明：on(type: 'error', callback: ErrorCallback<BusinessError>): void;  差异内容：atomicservice | api/@hms.ai.textToSpeech.d.ts |
| API从不支持元服务到支持元服务 | 类名：DownloadResponse；  API声明：off(type: 'error', callback?: ErrorCallback<BusinessError>): void;  差异内容：NA | 类名：DownloadResponse；  API声明：off(type: 'error', callback?: ErrorCallback<BusinessError>): void;  差异内容：atomicservice | api/@hms.ai.textToSpeech.d.ts |
