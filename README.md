# prometheus

* ひとまず自宅のルータを監視できるようにした。
* 監視対象のノードはprometheus.yamlに記載しているが、コンテナを停止せずに監視対象を追加することはできない・・・？（確認中）


## 用語

* exposition(開示): Prometheusがメトリクスをリイ用できる状態にするプロセスのこと
    * Prometheusに対するメトリクスの開示はHTTPを介して行われる。

## メトリクス名称の慣習

* メトリクス名はスネークケースで記載する。
* Counter, Summary, Histogram のメトリクスでは、_total, _count, _sum, _bucket というサフィックスを使う。
    * Counterで常に、_totalをつけることを除けばこれらのサフィックスはつけないようにするべき。
* 単位を一つに統一し、メトリクス名に含めるようにする。
    * 秒単位のカウンタには、mymetric_seconds_total など

## 参考

* 書籍：O'REILLY 入門 Prometheus
* [Blackbox Exporter で死活監視](https://qiita.com/Yohichi_Hayashi/items/05d5c9f45862958b9499)
* [Monitor Your Network With gNMI, SNMP, and Grafana](https://blog.networktocode.com/post/monitor_your_network_with_gnmi_snmp_and_grafana/)
* [InfluxDB+Telegraf+Grafanaによるネットワークモニタリング](https://www.janog.gr.jp/meeting/janog40/application/files/2815/0154/9553/janog40-SP3NM-tetsusat-01.pdf)