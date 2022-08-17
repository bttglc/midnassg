---
title: Sample Post
date: 12/01/2012
draft: False
---

[TOC]

# h1 Heading

## h2 Heading

### h3 Heading

#### h4 Heading

##### h5 Heading

###### h6 Heading


## lorem

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur? Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur?


## Text styling

| input                   | output                |
| ----------------------- | --------------------- |
| `**This is bold text**` | **This is bold text** |
| `_This is italic text_` | _This is italic text_ |


## Blockquotes

> Lorem ipsum dolor sit amet consectetur adipisicing elit. Esse suscipit nemo velit dignissimos deserunt, aliquid vitae architecto itaque dicta quidem. Natus voluptate atque minima temporibus eaque itaque repellendus voluptatum possimus?

## Lists

Unordered

- Create a list by starting a line with `+`, `-`, or `*`
- Sub-lists are made by indenting 2 spaces:
  - Marker character change forces new list start:
    - Ac tristique libero volutpat at
    * Facilisis in pretium nisl aliquet
    - Nulla volutpat aliquam velit

Ordered

1. Lorem ipsum dolor sit amet
2. Consectetur adipiscing elit
3. Integer molestie lorem at massa

## Code

Inline `code`

Syntax highlighting

```python3
@app.route("/")
def index():
    posts = []
    for post in listdir("posts"):
        post = getMetadata(post)
        if post["draft"] is False:
            posts.append(post)
    posts = sorted(
        posts, key=lambda d: datetime.strptime(d["date"], "%d/%m/%Y"), reverse=True
    )
    return render_template("index.html", posts=posts)
```

```java
java.io.FileNotFoundException: /etc/hadoop/conf/topology.table.file (No such file or directory)
at java.io.FileInputStream.open0(Native Method)
at java.io.FileInputStream.open(FileInputStream.java:195)
at java.io.FileInputStream.<init>(FileInputStream.java:138)
at java.io.FileInputStream.<init>(FileInputStream.java:93)
at org.apache.hadoop.net.TableMapping$RawTableMapping.load(TableMapping.java:103)
at org.apache.hadoop.net.TableMapping$RawTableMapping.resolve(TableMapping.java:129)
at org.apache.hadoop.net.CachedDNSToSwitchMapping.resolve(CachedDNSToSwitchMapping.java:119)
at org.apache.hadoop.yarn.util.RackResolver.coreResolve(RackResolver.java:101)
at org.apache.hadoop.yarn.util.RackResolver.resolve(RackResolver.java:81)
at org.apache.spark.scheduler.cluster.YarnScheduler.getRackForHost(YarnScheduler.scala:37)
at org.apache.spark.scheduler.TaskSchedulerImpl$$anonfun$resourceOffers$1.apply(TaskSchedulerImpl.scala:373)
at org.apache.spark.scheduler.TaskSchedulerImpl$$anonfun$resourceOffers$1.apply(TaskSchedulerImpl.scala:362)
at scala.collection.Iterator$class.foreach(Iterator.scala:891)
at scala.collection.AbstractIterator.foreach(Iterator.scala:1334)
at scala.collection.IterableLike$class.foreach(IterableLike.scala:72)
at scala.collection.AbstractIterable.foreach(Iterable.scala:54)
at org.apache.spark.scheduler.TaskSchedulerImpl.resourceOffers(TaskSchedulerImpl.scala:362)
at org.apache.spark.scheduler.cluster.CoarseGrainedSchedulerBackend$DriverEndpoint$$anonfun$2.apply(CoarseGrainedSchedulerBackend.scala:248)
at org.apache.spark.scheduler.cluster.CoarseGrainedSchedulerBackend$DriverEndpoint$$anonfun$2.apply(CoarseGrainedSchedulerBackend.scala:240)
at org.apache.spark.scheduler.cluster.CoarseGrainedSchedulerBackend.org$apache$spark$scheduler$cluster$CoarseGrainedSchedulerBackend$$withLock(CoarseGrainedSchedulerBackend.scala:693)
at org.apache.spark.scheduler.cluster.CoarseGrainedSchedulerBackend$DriverEndpoint.org$apache$spark$scheduler$cluster$CoarseGrainedSchedulerBackend$DriverEndpoint$$makeOffers(CoarseGrainedSchedulerBackend.scala:240)
at org.apache.spark.scheduler.cluster.CoarseGrainedSchedulerBackend$DriverEndpoint$$anonfun$receiveAndReply$1.applyOrElse(CoarseGrainedSchedulerBackend.scala:211)
at org.apache.spark.rpc.netty.Inbox$$anonfun$process$1.apply$mcV$sp(Inbox.scala:105)
at org.apache.spark.rpc.netty.Inbox.safelyCall(Inbox.scala:205)
at org.apache.spark.rpc.netty.Inbox.process(Inbox.scala:101)
at org.apache.spark.rpc.netty.Dispatcher$MessageLoop.run(Dispatcher.scala:221)
at java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1149)
at java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:624)
at java.lang.Thread.run(Thread.java:748)
```

## Tables

| Option | Description                                                               |
| ------ | ------------------------------------------------------------------------- |
| data   | path to data files to supply the data that will be passed into templates. |
| engine | engine to be used for processing templates. Handlebars is the default.    |
| ext    | extension to be used for dest files.                                      |

Right aligned columns

| Option |                                                               Description |
| -----: | ------------------------------------------------------------------------: |
|   data | path to data files to supply the data that will be passed into templates. |
| engine |    engine to be used for processing templates. Handlebars is the default. |
|    ext |                                      extension to be used for dest files. |

## Links

[link text](http://dev.nodeca.com)

## Horizontal Rules

---

## Images

![Stormtroopocat](/static/img/sample.png)


Footnote 1 link[^first].

To know more about other features consult [python-markdown](https://python-markdown.github.io/)'s website


[^first]: Footnotes **can have markup**
