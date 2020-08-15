# 패킷파일 설명
| 패킷 이름 | 내용 | 명령어 키워드 |
| ------ | ---------- | -------|
| 1_RequestConnectFromClient.pcap | 감염된 클라이언트가 세션생성 요청 | ii, inf |
| 2_Manager.pcap | Manager 메뉴 | Ex + fm, Ex + proc, Ex + tcp, Ex + rg, Ex + rs|
| 3_RunFile_link.pcap | 네트워크에 존재하는 파일실행 | rn + 실행포맷 + 실행경로 |
| 3_RunFile_localfile.pcap | 공격자 서버의 파일실행 | rn + 실행포맷 + 파일바이너리 |
| 3_RunFile_script.pcap | 스크립트 실행 | rn + 스크립트포맷 + 스크립트 내용 |

<br>


# 패킷 분석
## 1_RequestConnectFromClient
* njrat를 실행한 피해자가 공격자 서버와 세션연결 요청

![1_RequestConnectFromClient](images/1_RequestConnectFromClient.png)

<br> <br>

![1_RequestConnectFromClient_flow](images/1_RequestConnectFromClient_flow.png)


# 참고자료
* [1] njrat 스노트: https://github.com/dfirrequests/NetworkRequest/issues/1
* [2] security onion njrat 스노트 : /nsm/rules/downloads.rules