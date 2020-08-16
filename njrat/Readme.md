# 패킷파일 설명
| 패킷 이름 | 내용 | 명령어 키워드 |
| ------ | ---------- | -------|
| 1_RequestConnectFromClient.pcap | 감염된 클라이언트가 세션생성 요청 | ii, inf |
| 2_Manager.pcap | Manager 메뉴 | Ex + fm, Ex + proc, Ex + tcp, Ex + rg, Ex + rs|
| 3_RunFile_link.pcap | 네트워크에 존재하는 파일실행 | rn + 실행포맷 + 실행경로 |
| 3_RunFile_localfile.pcap | 공격자 서버의 파일실행 | rn + 실행포맷 + 파일바이너리 |
| 3_RunFile_script.pcap | 스크립트 실행 | rn + 스크립트포맷 + 스크립트 내용 |
| 4_RemoteCam | 원격 캠 제어 | 확인되지 않음(캠 없음) |
| 5_StealPassword.pcap | 패스워드 탈취 | ret |
| 6_keylogger.pcap | 키로거 | kl |
| 7_restart.pcap | njrat 재실행 | un + @ |
| 8_uninstall.pcap | njrat 삭제 | un + ~ |
| 9_CloseConnection | 연결종료 | un + ! |
| 10_RemoteDesktop.pcap | 원격 데스크톱 | sp(ck) |
| 11_chat | 채팅 | CH |


<br>

# Security onion 설정
1. (/etc/nsm/securityonion.conf) 사용자가 생성한 로컬규칙을 업데이트되도록 설정
```
LOCAL_NIDS_RULE_TUNING=yes
```
2. (/etc/nsm/rules/local.rules) 규칙 생성
3. (sudo rule-update) 작성한 규칙 업데이트
4. (sudo so-import-pcap) pcap파일 불러오기

<br>

# 참고자료
* [1] njrat 스노트: https://github.com/dfirrequests/NetworkRequest/issues/1
* [2] security onion njrat 스노트 : /etc/nsm/rules/downloads.rules