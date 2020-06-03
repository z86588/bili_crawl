CREATE TABLE `bili_ugc_rank` (
  `ugc_aid` int NOT NULL COMMENT '视频数字ID',
  `ugc_bvid` varchar(25) NOT NULL COMMENT '视频字符串ID',
  `ugc_author` varchar(20) NOT NULL COMMENT '视频作者',
  `ugc_coins` int NOT NULL COMMENT '视频投币数',
  `ugc_duration` varchar(10) NOT NULL COMMENT '视频总时长',
  `ugc_mid` int NOT NULL COMMENT '视频作者ID',
  `ugc_image` varchar(200) NOT NULL COMMENT '视频图片url',
  `ugc_play` int NOT NULL COMMENT '视频播放数',
  `ugc_pts` int NOT NULL COMMENT '视频综合得分',
  `ugc_title` varchar(100) NOT NULL COMMENT '视频标题',
  `ugc_review` int NOT NULL COMMENT '视频弹幕数',
  `ugc_rank` tinyint NOT NULL COMMENT '视频排行',
  `ugc_area` tinyint NOT NULL COMMENT '视频分类',
  `ugc_day` tinyint NOT NULL COMMENT '统计时间范围分类',
  `ugc_type` varchar(1) NOT NULL COMMENT '排行榜大类',
  `ugc_type_r` varchar(1) NOT NULL COMMENT '投稿时间分类',
  `ugc_crawl_time` date NOT NULL,
  PRIMARY KEY (`ugc_aid`,`ugc_type_r`,`ugc_type`,`ugc_day`,`ugc_area`,`ugc_crawl_time`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `bili_pgc_rank` (
  `pgc_badge` varchar(5) DEFAULT NULL COMMENT '付费范围',
  `pgc_copyright` varchar(15) DEFAULT NULL COMMENT '版权',
  `pgc_cover` varchar(200) DEFAULT NULL COMMENT '封面URL',
  `pgc_show` varchar(20) DEFAULT NULL COMMENT '信息',
  `pgc_pts` int DEFAULT NULL COMMENT '综合评分',
  `pgc_rank` tinyint DEFAULT NULL COMMENT '分类下排位',
  `pgc_sid` varchar(10) NOT NULL COMMENT '系列ID',
  `pgc_danmaku` int DEFAULT NULL COMMENT '弹幕数',
  `pgc_follow` int DEFAULT NULL COMMENT '追剧人数',
  `pgc_follow_s` int DEFAULT NULL COMMENT '系列追剧人数',
  `pgc_view` int DEFAULT NULL COMMENT '播放量',
  `pgc_title` varchar(100) DEFAULT NULL COMMENT '标题',
  `pgc_type_s` varchar(1) NOT NULL COMMENT '影视分类 season_type',
  `pgc_type_d` varchar(1) NOT NULL COMMENT '统计时间 day',
  `pgc_crawl_time` date NOT NULL,
  PRIMARY KEY (`pgc_sid`,`pgc_type_s`,`pgc_type_d`,`pgc_crawl_time`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;