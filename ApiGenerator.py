import time, os, re
from datetime import datetime
from os.path import isfile, join

CSS_STYLESHEET = """
body {
	background-color:#ffffff;
	color:#353833;
	font-family:Arial, Helvetica, sans-serif;
	font-size:76%;
	margin:0;
}
a:link, a:visited {
	text-decoration:none;
	color:#4c6b87;
}
a:hover, a:focus {
	text-decoration:none;
	color:#bb7a2a;
}
a:active {
	text-decoration:none;
	color:#4c6b87;
}
a[name] {
	color:#353833;
}
a[name]:hover {
	text-decoration:none;
	color:#353833;
}
pre {
	font-size:1.3em;
}
h1 {
	font-size:1.8em;
}
h2 {
	font-size:1.5em;
}
h3 {
	font-size:1.4em;
}
h4 {
	font-size:1.3em;
}
h5 {
	font-size:1.2em;
}
h6 {
	font-size:1.1em;
}
h7::first-line {
	
}
ul {
	list-style-type:disc;
}
code, tt {
	font-size:1.2em;
}
dt code {
	font-size:1.2em;
}
table tr td dt code {
	font-size:1.2em;
	vertical-align:top;
}
sup {
	font-size:.6em;
}
/*
Document title and Copyright styles
*/
.clear {
	clear:both;
	height:0px;
	overflow:hidden;
}
.aboutLanguage {
	float:right;
	padding:0px 21px;
	font-size:.8em;
	z-index:200;
	margin-top:-7px;
}
.legalCopy {
	margin-left:.5em;
}
.bar a, .bar a:link, .bar a:visited, .bar a:active {
	color:#FFFFFF;
	text-decoration:none;
}
.bar a:hover, .bar a:focus {
	color:#bb7a2a;
}
.tab {
	background-color:#0066FF;
	background-image:url(resources/titlebar.gif);
	background-position:left top;
	background-repeat:no-repeat;
	color:#ffffff;
	padding:8px;
	width:5em;
	font-weight:bold;
}
/*
Navigation bar styles
*/
.bar {
	background:#496b81;
	background-repeat:repeat-x;
	color:#FFFFFF;
	padding:.8em .5em .4em .8em;
	height:auto;/*height:1.8em;*/
	font-size:1em;
	margin:0;
}
.topNav {
	background-image:url(resources/background.gif);
	background-repeat:repeat-x;
	color:#FFFFFF;
	float:left;
	padding:0;
	width:100%;
	clear:right;
	height:2.8em;
	padding-top:10px;
	overflow:hidden;
}
.bottomNav {
	margin-top:10px;
	background-image:url(resources/background.gif);
	background-repeat:repeat-x;
	color:#FFFFFF;
	float:left;
	padding:0;
	width:100%;
	clear:right;
	height:2.8em;
	padding-top:10px;
	overflow:hidden;
}
.subNav {
	background-color:#dee3e9;
	border-bottom:1px solid #9eadc0;
	float:left;
	width:100%;
	overflow:hidden;
}
.subNav div {
	clear:left;
	float:left;
	padding:0 0 5px 6px;
}
ul.navList, ul.subNavList {
	float:left;
	margin:0 25px 0 0;
	padding:0;
}
ul.navList li{
	list-style:none;
	float:left;
	padding:3px 6px;
}
ul.subNavList li{
	list-style:none;
	float:left;
	font-size:90%;
}
.topNav a:link, .topNav a:active, .topNav a:visited, .bottomNav a:link, .bottomNav a:active, .bottomNav a:visited {
	color:#FFFFFF;
	text-decoration:none;
}
.topNav a:hover, .bottomNav a:hover {
	text-decoration:none;
	color:#bb7a2a;
}
.navBarCell1Rev {
	background-image:url(resources/tab.gif);
	background-color:#a88834;
	color:#FFFFFF;
	margin: auto 5px;
	border:1px solid #c9aa44;
}
/*
Page header and footer styles
*/
.header, .footer {
	clear:both;
	margin:0 20px;
	padding:5px 0 0 0;
}
.indexHeader {
	margin:10px;
	position:relative;
}
.indexHeader h1 {
	font-size:1.3em;
}
.title {
	color:#2c4557;
	margin:10px 0;
}
.subTitle {
	margin:5px 0 0 0;
}
.header ul {
	margin:0 0 25px 0;
	padding:0;
}
.footer ul {
	margin:20px 0 5px 0;
}
.header ul li, .footer ul li {
	list-style:none;
	font-size:1.2em;
}
/*
Heading styles
*/
div.details ul.blockList ul.blockList ul.blockList li.blockList h4, div.details ul.blockList ul.blockList ul.blockListLast li.blockList h4 {
	background-color:#dee3e9;
	border-top:1px solid #9eadc0;
	border-bottom:1px solid #9eadc0;
	margin:0 0 6px -8px;
	padding:2px 5px;
}
ul.blockList ul.blockList ul.blockList li.blockList h3 {
	background-color:#dee3e9;
	border-top:1px solid #9eadc0;
	border-bottom:1px solid #9eadc0;
	margin:0 0 6px -8px;
	padding:2px 5px;
}
ul.blockList ul.blockList li.blockList h3 {
	padding:0;
	margin:15px 0;
}
ul.blockList li.blockList h2 {
	padding:0px 0 20px 0;
}
/*
Page layout container styles
*/
.contentContainer, .sourceContainer, .classUseContainer, .serializedFormContainer, .constantValuesContainer {
	clear:both;
	padding:10px 20px;
	position:relative;
}
.indexContainer {
	margin:10px;
	position:relative;
	font-size:1.0em;
}
.indexContainer h2 {
	font-size:1.1em;
	padding:0 0 3px 0;
}
.indexContainer ul {
	margin:0;
	padding:0;
}
.indexContainer ul li {
	list-style:none;
}
.contentContainer .description dl dt, .contentContainer .details dl dt, .serializedFormContainer dl dt {
	font-size:1.1em;
	font-weight:bold;
	margin:10px 0 0 0;
	color:#4E4E4E;
}
.contentContainer .description dl dd, .contentContainer .details dl dd, .serializedFormContainer dl dd {
	margin:10px 0 10px 20px;
}
.serializedFormContainer dl.nameValue dt {
	margin-left:1px;
	font-size:1.1em;
	display:inline;
	font-weight:bold;
}
.serializedFormContainer dl.nameValue dd {
	margin:0 0 0 1px;
	font-size:1.1em;
	display:inline;
}
/*
List styles
*/
ul.horizontal li {
	display:inline;
	font-size:0.9em;
}
ul.inheritance {
	margin:0;
	padding:0;
}
ul.inheritance li {
	display:inline;
	list-style:none;
}
ul.inheritance li ul.inheritance {
	margin-left:15px;
	padding-left:15px;
	padding-top:1px;
}
ul.blockList, ul.blockListLast {
	margin:10px 0 10px 0;
	padding:0;
}
ul.blockList li.blockList, ul.blockListLast li.blockList {
	list-style:none;
	margin-bottom:25px;
}
ul.blockList ul.blockList li.blockList, ul.blockList ul.blockListLast li.blockList {
	padding:0px 20px 5px 10px;
	border:1px solid #9eadc0;
	background-color:#f9f9f9;
}
ul.blockList ul.blockList ul.blockList li.blockList, ul.blockList ul.blockList ul.blockListLast li.blockList {
	padding:0 0 5px 8px;
	background-color:#ffffff;
	border:1px solid #9eadc0;
	border-top:none;
}
ul.blockList ul.blockList ul.blockList ul.blockList li.blockList {
	margin-left:0;
	padding-left:0;
	padding-bottom:15px;
	border:none;
	border-bottom:1px solid #9eadc0;
}
ul.blockList ul.blockList ul.blockList ul.blockList li.blockListLast {
	list-style:none;
	border-bottom:none;
	padding-bottom:0;
}
table tr td dl, table tr td dl dt, table tr td dl dd {
	margin-top:0;
	margin-bottom:1px;
}
/*
Table styles
*/
.contentContainer table, .classUseContainer table, .constantValuesContainer table {
	border-bottom:1px solid #9eadc0;
	width:100%;
}
.contentContainer ul li table, .classUseContainer ul li table, .constantValuesContainer ul li table {
	width:100%;
}
.contentContainer .description table, .contentContainer .details table {
	border-bottom:none;
}
.contentContainer ul li table th.colOne, .contentContainer ul li table th.colFirst, .contentContainer ul li table th.colLast, .classUseContainer ul li table th, .constantValuesContainer ul li table th, .contentContainer ul li table td.colOne, .contentContainer ul li table td.colFirst, .contentContainer ul li table td.colLast, .classUseContainer ul li table td, .constantValuesContainer ul li table td{
	vertical-align:top;
	padding-right:20px;
}
.contentContainer ul li table th.colLast, .classUseContainer ul li table th.colLast,.constantValuesContainer ul li table th.colLast,
.contentContainer ul li table td.colLast, .classUseContainer ul li table td.colLast,.constantValuesContainer ul li table td.colLast,
.contentContainer ul li table th.colOne, .classUseContainer ul li table th.colOne,
.contentContainer ul li table td.colOne, .classUseContainer ul li table td.colOne {
	padding-right:3px;
}
.overviewSummary caption, .packageSummary caption, .contentContainer ul.blockList li.blockList caption, .summary caption, .classUseContainer caption, .constantValuesContainer caption {
	position:relative;
	text-align:left;
	background-repeat:no-repeat;
	color:#FFFFFF;
	font-weight:bold;
	clear:none;
	overflow:hidden;
	padding:0px;
	margin:0px;
}
caption a:link, caption a:hover, caption a:active, caption a:visited {
	color:#FFFFFF;
}
.overviewSummary caption span, .packageSummary caption span, .contentContainer ul.blockList li.blockList caption span, .summary caption span, .classUseContainer caption span, .constantValuesContainer caption span {
	white-space:nowrap;
	padding-top:8px;
	padding-left:8px;
	display:block;
	float:left;
	background-image:url(resources/titlebar.gif);
	height:18px;
}
.overviewSummary .tabEnd, .packageSummary .tabEnd, .contentContainer ul.blockList li.blockList .tabEnd, .summary .tabEnd, .classUseContainer .tabEnd, .constantValuesContainer .tabEnd {
	width:10px;
	background-image:url(resources/titlebar_end.gif);
	background-repeat:no-repeat;
	background-position:top right;
	position:relative;
	float:left;
}
ul.blockList ul.blockList li.blockList table {
	margin:0 0 12px 0px;
	width:100%;
}
.tableSubHeadingColor {
	background-color: #EEEEFF;
}
.altColor {
	background-color:#eeeeef;
}
.rowColor {
	background-color:#ffffff;
}
.overviewSummary td, .packageSummary td, .contentContainer ul.blockList li.blockList td, .summary td, .classUseContainer td, .constantValuesContainer td {
	text-align:left;
	padding:3px 3px 3px 7px;
}
th.colFirst, th.colLast, th.colOne, .constantValuesContainer th {
	background:#dee3e9;
	border-top:1px solid #9eadc0;
	border-bottom:1px solid #9eadc0;
	text-align:left;
	padding:3px 3px 3px 7px;
}
td.colOne a:link, td.colOne a:active, td.colOne a:visited, td.colOne a:hover, td.colFirst a:link, td.colFirst a:active, td.colFirst a:visited, td.colFirst a:hover, td.colLast a:link, td.colLast a:active, td.colLast a:visited, td.colLast a:hover, .constantValuesContainer td a:link, .constantValuesContainer td a:active, .constantValuesContainer td a:visited, .constantValuesContainer td a:hover {
	font-weight:bold;
}
td.colFirst, th.colFirst {
	border-left:1px solid #9eadc0;
	white-space:nowrap;
}
td.colLast, th.colLast {
	border-right:1px solid #9eadc0;
}
td.colOne, th.colOne {
	border-right:1px solid #9eadc0;
	border-left:1px solid #9eadc0;
}
table.overviewSummary  {
	padding:0px;
	margin-left:0px;
}
table.overviewSummary td.colFirst, table.overviewSummary th.colFirst,
table.overviewSummary td.colOne, table.overviewSummary th.colOne {
	width:25%;
	vertical-align:middle;
}
table.packageSummary td.colFirst, table.overviewSummary th.colFirst {
	width:25%;
	vertical-align:middle;
}
/*
Content styles
*/
.description pre {
	margin-top:0;
}
.deprecatedContent {
	margin:0;
	padding:10px 0;
}
.docSummary {
	padding:0;
}
/*
Formatting effect styles
*/
.sourceLineNo {
	color:green;
	padding:0 30px 0 0;
}
h1.hidden {
	visibility:hidden;
	overflow:hidden;
	font-size:.9em;
}
.block {
	display:block;
	margin:3px 0 0 0;
}
.strong {
	font-weight:bold;
}
.contentContainer .details dl dd {
    text-indent: -30px;
    position: relative;
    padding-left: 40px;
}"""

PROGRAM_HEAD = """
<!DOCTYPE html>
<!-- NewPage -->
<html lang="{0}">
<head>
<!-- Generated by ApiGenerator (version 1.0.1) on {1} -->
<title>{2}</title>
"""

INDEX_MAIN = """
<script type="text/javascript">
	tmpTargetPage = "" + window.location.search;
	if (tmpTargetPage != "" && tmpTargetPage != "undefined")
		tmpTargetPage = tmpTargetPage.substring(1);
	if (tmpTargetPage.indexOf(":") != -1 || (tmpTargetPage != "" && !validURL(tmpTargetPage)))
		tmpTargetPage = "undefined";
	targetPage = tmpTargetPage;
	function validURL(url) {
		try {
			url = decodeURIComponent(url);
		}
		catch (error) {
			return false;
		}
		var pos = url.indexOf(".html");
		if (pos == -1 || pos != url.length - 5)
			return false;
		var allowNumber = false;
		var allowSep = false;
		var seenDot = false;
		for (var i = 0; i < url.length - 5; i++) {
			var ch = url.charAt(i);
			if ('a' <= ch && ch <= 'z' ||
					'A' <= ch && ch <= 'Z' ||
					ch == '$' ||
					ch == '_' ||
					ch.charCodeAt(0) > 127) {
				allowNumber = true;
				allowSep = true;
			} else if ('0' <= ch && ch <= '9'
					|| ch == '-') {
				if (!allowNumber)
					 return false;
			} else if (ch == '/' || ch == '.') {
				if (!allowSep)
					return false;
				allowNumber = false;
				allowSep = false;
				if (ch == '.')
					 seenDot = true;
				if (ch == '/' && seenDot)
					 return false;
			} else {
				return false;
			}
		}
		return true;
	}
	function loadFrames() {
		if (targetPage != "" && targetPage != "undefined")
			 top.classFrame.location = top.targetPage;
	}
</script></head>
<frameset cols="20%,80%" title="Documentation frame" onload="top.loadFrames()">
<frameset rows="100%" title="Left frames" onload="top.loadFrames()">
<frame src="allclasses-frame.html" name="packageFrame" title="All classes">
</frameset>
<frame src="overview-summary.html" name="classFrame" title="Package and class descriptions" scrolling="yes">
<noframes>
<noscript>
<div>JavaScript is disabled on your browser.</div>
</noscript>
<h2>Frame Alert</h2>
<p>This document is designed to be viewed using the frames feature. If you see this message, you are using a non-frame-capable web client. Link to <a href="overview-summary.html">Non-frame version</a>.</p>
</noframes>
</frameset>
</html>"""

ALL_CLASSES_MAIN = """
<link rel="stylesheet" type="text/css" href="stylesheet.css" title="Style">
<script>window.ohcglobal || document.write('<script src="/en/dcommon/js/global.js">\\x3C/script>')</script></head>
<body>
<h1 class="bar">All Classes</h1>
<div class="indexContainer">
<ul>"""

CLASS = """<li><a href="{0}.html" title="class in {1}" target="classFrame">{0}</a></li>\n"""
CURSIVE_CLASS = """<li><a href="{0}.html" title="class in {1}" target="classFrame"><i>{0}</i></a></li>\n"""

ALL_CLASSES_END = """
</ul>
</div>
</body>
</html>"""

CLASS_0 = """
<link rel="stylesheet" type="text/css" href="stylesheet.css" title="Style">
<script>window.ohcglobal || document.write('<script src="/en/dcommon/js/global.js">\\x3C/script>')</script>
</head>
<body>
<script type="text/javascript"><!--
	if (location.href.indexOf('is-external=true') == -1) {"""

CLASS_0_1 = """
</script>
<noscript>
<div>JavaScript is disabled on your browser.</div>
</noscript>
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="subTitle">{0}</div>
<h2 title="Class {1}" class="title">Class {1}</h2>
</div>
<div class="contentContainer">"""

CLASS_1 = """
<ul class="inheritance">
<li><a href="{0}.html" title="class in {1}">{2}</a></li>
<li>"""

CLASS_2 = """
<ul class="inheritance">
<li>{0}</li>
</ul>"""

CLASS_3 = """<a href="{0}.html" title="class in {1}">{0}</a>"""
CLASS_3_1 = """, <a href="{0}.html" title="class in {1}">{0}</a>"""

CLASS_4 = """
<hr>
<br>
<pre>public abstract class <span class="strong">{0}</span>"""

CLASS_5 = """<a href="{0}.html" title="class in {1}">{0}</a>"""
CLASS_5_1 = """, <a href="{0}.html" title="class in {1}">{0}</a>"""

ALT_COLOR = '\n<tr class="altColor">'
ROW_COLOR = '\n<tr class="rowColor">'

SUMMARY_1 = """
<div class="summary">
<ul class="blockList">
<li class="blockList">"""

FIELD_SUMMARY_1 = """
<!-- =========== FIELD SUMMARY =========== -->
<ul class="blockList">
<li class="blockList"><a name="field_summary">
<!--   -->
</a>
<h3>Field Summary</h3>"""

FIELD_SUMMARY_1_2 = """
<table class="overviewSummary" border="0" cellpadding="3" cellspacing="0" summary="Field Summary table, listing fields, and an explanation">
<caption><span>Fields</span><span class="tabEnd">&nbsp;</span></caption>
<tr>
<th class="colFirst" scope="col">Modifier and Type</th>
<th class="colLast" scope="col">Field and Description</th>
</tr>"""

FIELD_SUMMARY_2 = """
<td class="colFirst"><code>{2} {3}</code></td>
<td class="colLast"><code><strong><a href="{0}.html#{1}">{1}</a></strong>"""

FIELD_SUMMARY_2_p = """
<td class="colFirst"><code>{2} [{3}]</code></td>
<td class="colLast"><code><strong><a href="{0}.html#{1}">{1}</a></strong>"""

FIELD_SUMMARY_2_1 = """
<td class="colFirst"><code>{2} <a href="{3}.html" title="class in {4}">{3}</a></code></td>
<td class="colLast"><code><strong><a href="{0}.html#{1}">{1}</a></strong>"""

FIELD_SUMMARY_2_1_p = """
<td class="colFirst"><code>{2} [<a href="{3}.html" title="class in {4}">{3}</a>]</code></td>
<td class="colLast"><code><strong><a href="{0}.html#{1}">{1}</a></strong>"""

FIELD_SUMMARY_3 = """</code>
<div class="block">{0}</div>
</td>
</tr>"""

FIELDS_INHERITED_1 = """
<ul class="blockList">
<li class="blockList"><a name="fields_inherited_from_class_{0}.{1}">
<!--   -->
</a>
<h3>Fields inherited from class&nbsp;{0}.<a href="{1}.html" title="class in {0}">{1}</a></h3>
<code>"""

FIELDS_INHERITED_2 = """<a href="{0}.html#{1}">{1}</a>"""
FIELDS_INHERITED_2_1 = """, <a href="{0}.html#{1}">{1}</a>"""

CONSTRUCTOR_SUMMARY_1 = """
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<ul class="blockList">
<li class="blockList"><a name="constructor_summary">
<!--   -->
</a>
<h3>Constructor{0}</h3>
<table class="overviewSummary" border="0" cellpadding="3" cellspacing="0" summary="Constructor Summary table, listing constructors, and an explanation">
<caption><span>Constructor</span><span class="tabEnd">&nbsp;</span></caption>
<tr>
<th class="colOne" scope="col">Constructor and Description</th>
</tr>"""

CONSTRUCTOR_SUMMARY_1_bis = """ inherited from <a href="{0}.html#{0}">{0}</a>"""

CONSTRUCTOR_SUMMARY_2 = """
<tr class="altColor">
<td class="colOne"><code><strong><a href="{0}.html#{0}">{0}</a></strong>("""

CONSTRUCTOR_SUMMARY_3 = """<a href="{0}.html" title="class in {1}">{0}</a>&nbsp;{2}"""

CONSTRUCTOR_SUMMARY_3_p = """[<a href="{0}.html" title="class in {1}">{0}</a>]&nbsp;{2}"""

CONSTRUCTOR_SUMMARY_3_1 = "{0}&nbsp;{1}"

CONSTRUCTOR_SUMMARY_3_1_p = "[{0}]&nbsp;{1}"

CONSTRUCTOR_SUMMARY_4 = """, <a href="{0}.html" title="class in {1}">{0}</a>&nbsp;{2}"""

CONSTRUCTOR_SUMMARY_4_p = """, [<a href="{0}.html" title="class in {1}">{0}</a>]&nbsp;{2}"""

CONSTRUCTOR_SUMMARY_4_1 = """, {0}&nbsp;{1}"""

CONSTRUCTOR_SUMMARY_4_1_p = """, [{0}]&nbsp;{1}"""

CONSTRUCTOR_SUMMARY_5 = """)</code>
<div class="block">{0}</div>
</td>
</tr>"""

METHOD_SUMMARY_1 = """
<!-- ========== METHOD SUMMARY =========== -->
<ul class="blockList">
<li class="blockList"><a name="method_summary">
<!--   -->
</a>
<h3>Method Summary</h3>
<table class="overviewSummary" border="0" cellpadding="3" cellspacing="0" summary="Method Summary table, listing methods, and an explanation">
<caption><span>Methods</span><span class="tabEnd">&nbsp;</span></caption>
<tr>
<th class="colFirst" scope="col">Modifier and Type</th>
<th class="colLast" scope="col">Method and Description</th>
</tr>"""

METHOD_SUMMARY_2 = """
<td class="colFirst"><code>{2} {3}</code></td>
<td class="colLast"><code><strong><a href="{0}.html#{1}">{1}</a></strong>("""

METHOD_SUMMARY_2_p = """
<td class="colFirst"><code>{2} [{3}]</code></td>
<td class="colLast"><code><strong><a href="{0}.html#{1}">{1}</a></strong>("""

METHOD_SUMMARY_2_1 = """
<td class="colFirst"><code>{2} <a href="{3}.html" title="class in {4}">{3}</a></code></td>
<td class="colLast"><code><strong><a href="{0}.html#{1}">{1}</a></strong>("""

METHOD_SUMMARY_2_1_p = """
<td class="colFirst"><code>{2} [<a href="{3}.html" title="class in {4}">{3}</a>]</code></td>
<td class="colLast"><code><strong><a href="{0}.html#{1}">{1}</a></strong>("""

METHOD_SUMMARY_3 = """<a href="{0}.html" title="class in {1}">{0}</a>&nbsp;{2}"""

METHOD_SUMMARY_3_p = """[<a href="{0}.html" title="class in {1}">{0}</a>]&nbsp;{2}"""

METHOD_SUMMARY_3_1 = "{0}&nbsp;{1}"

METHOD_SUMMARY_3_1_p = "[{0}]&nbsp;{1}"

METHOD_SUMMARY_4 = """, <a href="{0}.html" title="class in {1}">{0}</a>&nbsp;{2}"""

METHOD_SUMMARY_4_p = """, [<a href="{0}.html" title="class in {1}">{0}</a>]&nbsp;{2}"""

METHOD_SUMMARY_4_1 = """, {0}&nbsp;{1}"""

METHOD_SUMMARY_4_1_p = """, [{0}]&nbsp;{1}"""

METHOD_SUMMARY_5 = """)</code>
<div class="block">{0}</div>
</td>
</tr>"""

METHODS_INHERITED_1 = """
<ul class="blockList">
<li class="blockList"><a name="methods_inherited_from_class_{0}.{1}">
<!--   -->
</a>
<h3>Methods inherited from class&nbsp;{0}.<a href="{1}.html" title="class in {0}">{1}</a></h3>
<code>"""

METHODS_INHERITED_2 = """<a href="{0}.html#{1}">{1}</a>"""
METHODS_INHERITED_2_1 = """, <a href="{0}.html#{1}">{1}</a>"""

DETAILS_1 = """
<div class="details">
<ul class="blockList">
<li class="blockList">
"""

FIELD_DETAIL_1 = """
<!-- ============ FIELD DETAIL =========== -->
<ul class="blockList">
<li class="blockList"><a name="field_detail">
<!--   -->
</a>
<h3>Field Detail</h3>"""

FIELD_DETAIL_2 = """
<a name="{0}">
<!--   -->
</a>
<ul class="blockList">
<li class="blockList">
<h4>{0}</h4>"""

FIELD_DETAIL_3_1 = """
<pre>{1}&nbsp;{2} {0}</pre>
<div class="block">{3}</div>
</li>
</ul>"""

FIELD_DETAIL_3_1_p = """
<pre>{1}&nbsp;[{2}] {0}</pre>
<div class="block">{3}</div>
</li>
</ul>"""

FIELD_DETAIL_3_2 = """
<pre>{1}&nbsp;<a class="api_link" href="{2}.html" title="class in {3}">{2}</a> {0}</pre>
<div class="block">{4}</div>
</li>
</ul>"""

FIELD_DETAIL_3_2_p = """
<pre>{1}&nbsp;[<a class="api_link" href="{2}.html" title="class in {3}">{2}</a>] {0}</pre>
<div class="block">{4}</div>
</li>
</ul>"""

CONSTRUCTOR_DETAIL_1 = """
<!-- ========= CONSTRUCTOR DETAIL ======== -->
<ul class="blockList">
<li class="blockList"><a name="constructor_detail">
<!--   -->
</a>
<h3>Constructor Detail</h3>"""

CONSTRUCTOR_DETAIL_2 = """
<a name="{0}">
<!--   -->
</a>
<ul class="blockList">
<li class="blockList">
<h4>{0}</h4>
<pre>public&nbsp;{0}({1})</pre>
<div class="block">{2}</div>"""

METHOD_DETAIL_1 = """
<!-- ============ METHOD DETAIL ========== -->
<ul class="blockList">
<li class="blockList"><a name="method_detail">
<!--   -->
</a>
<h3>Method Detail</h3>"""

METHOD_DETAIL_2 = """
<a name="{0}">
<!--   -->
</a>
<ul class="blockList">
<li class="blockList">
<h4>{0}</h4>"""

METHOD_DETAIL_3_1 = """<pre>{0}&nbsp;{1}&nbsp;{2}("""

METHOD_DETAIL_3_1_p = """<pre>{0}&nbsp;[{1}]&nbsp;{2}("""

METHOD_DETAIL_3_2 = """
<pre>{0}&nbsp;<a href="{1}.html" title="class in {2}">{1}</a>&nbsp;{3}("""

METHOD_DETAIL_3_2_p = """
<pre>{0}&nbsp;[<a href="{1}.html" title="class in {2}">{1}</a>]&nbsp;{3}("""

METHOD_DETAIL_4 = """{0})</pre>
<div class="block">{1}</div>"""

METHOD_DETAIL_PARAMETRES_1 = """<dt><span class="strong">Parameters:</span></dt>"""

METHOD_DETAIL_PARAMETRES_2 = """<dd>{0} - {1}</dd>"""

METHOD_DETAIL_THROWS_1 = """<dt><span class="strong">Throws:</span></dt>"""

METHOD_DETAIL_THROWS_2_1 = """<dd><a href="{0}.html" title="class in {1}">{0}</a> - {2}</dd>"""

METHOD_DETAIL_THROWS_2_2 = """<dd>{0} - {1}</dd>"""

INFO_API_LINK = """<a class="api_link" href="{0}.html" title="class in {1}">{2}</a>"""
INFO_API_METHOD_LINK = """<a class="api_link" href="{0}.html#{1}">{1}()</a>"""
INFO_API_FIELD_LINK = """<a class="api_link" href="{0}.html#{1}">{1}</a>"""
INFO_WEB_LINK_S = """<a class="web_link" href="{0}">{1}</a>""" #Opens the dir in the api itself, may cause problems, depending on the page
INFO_WEB_LINK_O = """<a class="web_link" href="{0}" target="_blank">{1}</a>""" #Opens the dir in another tab
INFO_WEB_LINK_P = """<a class="web_link" href="{0}" target="_top">{1}</a>""" #Opens the dir in the same tab
INFO_WEB_LINK_V = """<a class="web_link" href="javascript:window.open('{0}','','toolbar=yes');void 0">{1}</a>"""

#USER INFO:
#[rootPath, proyectName, authorNames, version, realise, language, tabulations, privateMethods, links]

#CLASSES:
"""
General: [[className, classDir, [superClassCompound...], classInfo, [classField...], constructor, [method...], [subClassID...]]...]
-className: ClassName
-classDir: LibName.ProgramName.ClassName
-superClassCompound: [superClassName, "self/super"] The self/super is depending on if the super is direcly related with the class. |Up until the returned list of getClasifiedInfo its only the names who appears in the definition, not the all of them|
-classInfo: ClassInfo (Written in the next line of the definition of the class between triple ")
-classField: [modifier, type, name, value, info].|Up until the returned list of getUsefullInfoFromLibraryInfo the info var contains all the info of the field
-constructor: method(The name is changed to the name of the class and it is added to the constructor place)
-method: [modifier, type, name, inputVars, info, version, typeInfo, summary, [throw]]
**inputVars: [type, name, predef, info].|Up until the returned list of getUsefullInfoFromLibraryInfo its formed of: [name, predef]|
-subClassID: Id of the sub class that inherits from this class It was added to the end because of structural purposes (I forgetted, and I'm lazy)
-throw: [Exception, info]
"""

#TEST:
"""
>>> class A:
	pass

>>> class B(A):
	pass

>>> class C(B):
	pass

>>> class D:
	pass

>>> class E(D, C):
	pass

"""
DEFAULT_CONSTRUCTOR = ['', '', 'NAME', [], '', '', '', '', [[], []]]
SELF_STRUCTURE = ['', 'self', '', '']

DEFAULT_STRUCTURES = ["int", "float", "complex", "list", "tuple", "string", "char", "set", "dictionary", "dict"]

PRINT = False

def main():

	#Getting info from the user
	userInfo = [] 
	userInfo = askInfo()
	#"C:\\Python\\Lib"
	#"C:\\Users\\pabri\\Desktop\\Programacion\\Python programing\\Escritorio\\PySwing"
	#userInfo = ["C:\\Users\\pabri\\Desktop\\Programacion\\Python programing\\Escritorio\\PySwing", "PySwing", ["Pablo Rivero Lazaro"], "1.0", "1.0.1", "English", ["	", "    "], False, True]
	try:
		if not userInfo:
			print("Creation of the Api cancelled")
			time.sleep(0.5)
			return
	except:
		pass
	#print(userInfo)

	#Generating the main html files
	rute = generateMainHTML(userInfo)

	#Obtaining info from the library
	preClasses = []
	if PRINT: print("Obtaining info from the library")
	if PRINT: print()
	preClasses = getLibraryInfo(rute, userInfo)
	#print(preClasses)

	#Obtaining info from the methods of the library
	if PRINT: print("Obtaining info from the methods of the library")
	if PRINT: print()

	#Obtaining the usefull info from the library
	preClasses = getUsefullInfoFromLibraryInfo(preClasses)
	#print(classes)

	#Clasifing the info obtained
	classes = []
	classes = getClasifiedInfo(userInfo, preClasses)

	#Organizeing the info obtained
	classes = getOrganizedInfo(classes)
	if classes == False:
		if PRINT: print("Creation of the Api auto cancelled")
		time.sleep(5)
		return
	if PRINT: print(classes)
	#print(classes)

	generateApi(rute, userInfo, classes)

def askInfo():
	def testExit(text):
		if "/Exit" in text: return True
		return False

	print("Now some questions will be asked to generate properly the documentation")
	print("If you want to quit, at any moment write /Exit\n")

	#Root path
	rootPath = str(input("Root path for the documentation [.]:"))
	if testExit(rootPath): return False
	rootPath = rootPath.strip()
	print()
	
	#Proyect name
	while True:
		proyectName = str(input("Project name:"))
		if testExit(proyectName): return False
		if proyectName == "": print("You have to give the project a name")
		else: break
	proyectName = proyectName.strip()
	print()

	#Author names Pablo Rivero Lazaro, Daniel Felipe Cordero, Cristobal Orihuela Garcia
	while True:
		authorNames = str(input("Author names (Name Surnames, Name2 Surnames2...):"))
		if testExit(authorNames): return False
		if authorNames == "": print("The documentation has to have at least one author")
		else: break
	authorNames = authorNames.split(", ")
	print()

	#Version & realise
	print("""ApiGenerator has the notion of a "version" and a "realise" for the\nsoftware. Each version can have multiple realises. For example, for Python the\nversion is something like 2.5 or 3.0, while the release is something like 2.5.1\nor 3.0a1. If you don't need this dual structure, just set both to the same value""")
	version = str(input("Project version:"))
	if testExit(version): return False
	version = version.strip()
	realise = str(input("Project realise:"))
	if testExit(realise): return False
	realise = realise.strip()
	print()

	#Lenguage
	print("If the documentation is written in other language that English, you can select a language here")
	language = str(input("Project language [en]:"))
	if testExit(language): return False
	if language == "": language = "English"
	language = language.strip()
	print()

	#Tabulations
	print("""You have to indicate all the types of tabulations that you have\nused, if you don't know what types of tabulations you have used, just go to\nthe programs you have used to make the code of ALL the python files you\nhave, open a new file, press the key tab and copy what you have just added\nto the new file, then paste this to this question. Do this with all the\nprograms you had used. When you finish, write f and press intro.""")
	tabulations = []
	while True:
		newTabulation = str(input("Enter your tabulation:"))
		if testExit(newTabulation): return False
		if newTabulation != "f": tabulations.append(newTabulation)
		else: break
	print()

	#HTML creation
	while True:
		privateMethods = str(input("Do you want the private methods to appear in the api (y/n) [n]:"))
		if testExit(privateMethods): return False
		if privateMethods == "y":
			privateMethods = True
			break

		elif privateMethods == "n" or privateMethods == "":
			privateMethods = False
			break

		else:
			print("You have to write y(Yes) or n(No)")
	print()

	while True:
		links = str(input("Do you want to inclue the functionality of adding links between the api itself (y/n) [n]:"))
		if testExit(links): return False
		if links == "y":
			links = True
			break

		elif links == "n" or links == "":
			links = False
			break

		else:
			print("You have to write y(Yes) or n(No)")
	print()

	return [rootPath, proyectName, authorNames, version, realise, language, tabulations, privateMethods, links]

def generateMainHTML(userInfo):
	if PRINT: print("Creating index.html and stylesheet")

	#Carpeta de la api
	if userInfo[0] == "": ruta = os.getcwd() + "\\"
	else: ruta = userInfo[0] + "\\"
	if not os.path.isdir(ruta + userInfo[1] + "_Api"): os.mkdir(ruta + userInfo[1] + "_Api")
	rutaApi = ruta + userInfo[1] + "_Api" + "\\"
	index = open(rutaApi + "index.html", "w") #Sat Oct 06 06:48:55 PDT 2018
	program_head = PROGRAM_HEAD.format(userInfo[5], datetime.now(), userInfo[1] + " Api")
	index.write(program_head)
	index.write(INDEX_MAIN)
	index.close()
	stylesheet = open(rutaApi + "stylesheet.css", "w")
	stylesheet.write(CSS_STYLESHEET)
	stylesheet.close()
	if PRINT: print("Finished creation of index.html and stylesheet")
	return rutaApi

def getLibraryInfo(rute, userInfo):
	def discardNoPythonFiles(files):
		pyFiles = []
		for file in files:
			if file.endswith(".py"):
				pyFiles.append(file)

		return pyFiles

	classes = []
	files = [arch for arch in os.listdir(userInfo[0]) if isfile(join(userInfo[0], arch))]
	files = discardNoPythonFiles(files)

	#File by file, extracting all the usefull information
	for file in files:
		actualClass = ["", "", [], "", [], "", [], []]
		actualFunction = ["", "", "", [], "", "", "", "", [[], []]]

		#Opening the file
		if PRINT: print("Reading file:" + file)
		opened = open(userInfo[0] + "\\" + file)

		#Reading the first line
		l = 0
		try:
			line = opened.readline()

		except UnicodeDecodeError as e:
			if PRINT: print("While decoding the file:" + str(file) + ", an unespected UnicodeDecodeError happended\nThis will not affect to the creation of the api, but it could make something in the Api to look bad\nPlease check out the Api")
			if PRINT: print("Raw error:" + str(e))

		inClass = False
		classTabs = 0
		inFunction = False
		functionTabs = 0

		#Comments
		expectingClassInfo = False
		expectingFunctionInfo = False
		inClassComment = False
		inFunctionComment = False
		classComment = ""
		functionComment = ""

		#Reading all the files
		while line != "":

			#Getting the tabulation
			tabs = 0
			for tabulation in userInfo[6]:
				if line.startswith(tabulation):
					tabs = line.count(tabulation)
					break

			#Preparing the lines to be understanded
			if line.endswith("\n"): line = line.rstrip("\n")
			line = line.strip()
			if "h" + line + "h" != "hh":

				#Exited the class
				if inClass and tabs < classTabs:
					inClass = False
					classTabs = 0
					if inFunction:
						inFunction = False
						functionTabs = 0
						actualClass[6].append(actualFunction)

						actualFunction = ["", "", "", [], "", "", "", "", [[], []]]

					classes.append(actualClass)
					actualClass = ["", "", [], "", [], "", [], []]

				#Exited the function
				if inFunction and tabs < functionTabs:
					inFunction = False
					functionTabs = 0
					if inClass:
						actualClass[6].append(actualFunction)

					else:
						pass
						#It is a function out a class

					actualFunction = ["", "", "", [], "", "", "", "", [[], []]]

				#In a class
				if inClass:

					#In a class and in a function
					if inFunction:
						if expectingFunctionInfo:
							if line.startswith('"""'): #It's the comment line we are specting
								inFunctionComment = True
								expectingFunctionInfo = False
								extractingLine = line.lstrip('"""')

						else:
							extractingLine = line

						if inFunctionComment:
							if extractingLine.endswith('"""'): #The comment lasts only one line
								inFunctionComment = False
								extractingLine = extractingLine.rstrip('"""')

							if extractingLine != "": #There is more that just the intro for the comment
								for char in extractingLine:
									functionComment = functionComment+char
								functionComment+=" "

							if not inFunctionComment:
								actualFunction[4] = functionComment
								functionComment = ""


					#In a  class, but not in a function
					else:
						if expectingClassInfo:
							if line.startswith('"""'): #It's the comment line we are specting
								inClassComment = True
								expectingClassInfo = False
								extractingLine = line.lstrip('"""')

						elif not inClassComment and not line.startswith("#"): #It's a constant
							defLine = line
							name = ""
							value = ""
							comment = ""

							#Extracting name
							for char in line:
								if char == ' ': break
								else: name+=char
							line = line.lstrip(name)
							line = line.lstrip()

							#Extracting value if it exists
							if len(line) > 0 and line[0] == '=':
								line = line.lstrip('=')
								line = line.lstrip()
								inPar = 0
								for char in line:
									if char == '(': inPar+=1
									elif char == ')': inPar-=1
									if char == ' ' or char == '#':
										if inPar == 0: break
										else: value+=char
									else: value+=char
								line = line.lstrip(value)
								line = line.lstrip()

								#Extracting comment
								if line.startswith('#'):
									line = line.lstrip('#')
									line = line.lstrip()
									for char in line:
										comment+=char
									comment = comment.rstrip()

								#Saving the adquired info
								actualClass[4].append(["", "", name, value, comment])
							else: line = defLine

						else:
							extractingLine = line

						if inClassComment:
							if extractingLine.endswith('"""'): #The comment lasts only one line
								inClassComment = False
								extractingLine = extractingLine.rstrip('"""')

							if extractingLine != "": #There is more that just the intro for the comment
								for char in extractingLine:
									classComment = classComment+char
								classComment+=" "

							if not inClassComment:
								actualClass[3] = classComment
								classComment = ""

				#In a function, but not in class
				elif inFunction:
					pass

				#Nor in a function or class
				else:
					pass

				#Entering a function
				if inClass and line.startswith("def") and not inClassComment and not inFunctionComment and tabs == classTabs:
					inFunction = True
					functionTabs = tabs+1
					end = False
					expectingFunctionInfo = True
					expectingClassInfo = False
					if PRINT: print("*", end = "")

					#Preparing line
					extractingLine = line.lstrip("def")
					extractingLine = extractingLine.lstrip()

					#Extracting name
					name = ""
					for char in extractingLine:
						if char == '(' or char == ' ':
							break

						elif char == ':':
							end = True
							break

						else:
							name = name+char
					extractingLine = extractingLine.lstrip(name)
					extractingLine = extractingLine.lstrip()

					#Extracting parameters
					parameters = []
					if not end:
						parameter = ["", ""]#[name, predefValue]
						inNames = False
						inPredef = False
						inDepth = 0 #Number of parenthesis or others
						for char in extractingLine:
							if inNames and inPredef:
								if char == '(' or char == '[' or char == '{':
									inDepth+=1

								elif char == ')' or char == ']' or char == '}':
									if inDepth > 0:
										inDepth-=1

										if inDepth == 0:
											parameter[1] = parameter[1]+char

							if char == ')' and inDepth == 0:
								if parameter != ["", ""]: parameters.append(parameter)
								break

							elif char == ',' and parameter != ["", ""] and inDepth == 0:
								parameters.append(parameter)
								parameter = ["", ""]
								inPredef = False

							elif inPredef and char != ' ':
								parameter[1] = parameter[1]+char

							elif inPredef and inDepth > 0:
								parameter[1] = parameter[1]+char

							if inNames and char != ' ' and not inPredef and char != ',':
								if char == '=':
									inPredef = True

								else:
									parameter[0] = parameter[0]+char

							inNames = True

					actualFunction[2] = name
					actualFunction[3] = parameters

				#Entering a spare function
				elif line.startswith("def") and not inClassComment and not inFunctionComment:
					pass

				#Entering a class
				if line.startswith("class") and not inClassComment and not inFunctionComment and not inClass: #Classes inside classes are not permited
					inClass = True
					classTabs = tabs+1
					end = False
					expectingClassInfo = True
					if PRINT: print(".", end = "")

					#Preparing line
					extractingLine = line.lstrip("class")
					extractingLine = extractingLine.lstrip()

					#Extracting name
					name = ""
					for char in extractingLine:
						if char == '(' or char == ' ':
							break

						elif char == ':':
							end = True
							break

						else:
							name = name+char
					if PRINT: print(name)
					extractingLine = extractingLine.lstrip(name)
					extractingLine = extractingLine.lstrip()

					#Extracting supers
					superClasses = []
					if not end:
						superClass = ""
						inName = False
						for char in extractingLine:
							if char == ')':
								if superClass != "": superClasses.append(superClass)
								break

							elif char == ',' and superClass != "":
								superClasses.append(superClass)
								superClass = ""

							if inName and char != ' ' and char != ',':
								superClass = superClass+char

							inName = True

					actualClass[0] = name
					actualClass[1] = userInfo[1] + "." + file.rstrip(".py") + "." + name
					actualClass[2] = superClasses

			#Reading new line
			l+=1
			try:
				line = opened.readline()

			except UnicodeDecodeError as e:
				if PRINT: print("While decoding the file:" + str(file) + ", an unespected UnicodeDecodeError happended\nThis will not affect to the creation of the api, but it could make something in the Api to look bad\nPlease check out the Api")
				if PRINT: print("Raw error:" + str(e))

		if actualClass != ["", "", [], "", [], "", [], []]:
			if inFunction:
				actualClass[6].append(actualFunction)

			classes.append(actualClass)

		elif actualFunction != ["", "", "", [], "", "", "", "", [[], []]]:
			pass
			#It is a function out a class

		if PRINT: print()
		opened.close()

	return classes

def getUsefullInfoFromLibraryInfo(libraryInfo):

	#DATA:
	#[modifier, type, info, version, [inputVarInfo, ...]]

	#INPUT VAR INFO:
	#[name, type, info]

	def foundVarName(inputVars, name):
		i = 0
		for var in inputVars:
			if str(var[0]) == str(name):
				return i
			i+=1
		return -1

	#Extracting info from fields
	rLibraryInfo = libraryInfo
	classIndex = 0
	for cls in libraryInfo:
		if PRINT: print("Decoding info from fields of: " + cls[0])
		fieldIndex = 0
		for field in cls[4]:
			data = ["", "", field[2], field[3], ""]
			if PRINT: print("*", end = "")
			possibleInfo = False
			possibleType = ""
			dataType = 0 #1-type, 2-modifier, 3-info
			actualData = ""
			for char in field[4]:
				if possibleInfo and not char == ':': possibleType+=char
				elif char == ';' and dataType != 0:
					if dataType == 1: #Type
						data[1] = actualData.strip()
						dataType = 0
						actualData = ""

					elif dataType == 2: #Modifier
						data[0] = actualData.strip()
						dataType = 0
						actualData = ""

					elif dataType == 3: #Info
						data[4] = actualData.strip()
						dataType = 0
						actualData = ""

				elif dataType != 0:
					if dataType == 3 or not char == ':': actualData+=char

				elif char == ':':
					if not possibleInfo: possibleInfo = True
					elif possibleType == "type":
						dataType = 1
						possibleInfo = False
						possibleType = ""

					elif possibleType == "modifier":
						dataType = 2
						possibleInfo = False
						possibleType = ""

					elif possibleType == "info":
						dataType = 3
						possibleInfo = False
						possibleType = ""

			if actualData != "":
				if dataType == 1: data[1] = actualData.strip()
				elif dataType == 2: data[0] = actualData.strip()
				elif dataType == 3: data[4] = actualData.strip()

			rLibraryInfo[classIndex][4][fieldIndex] = data
			fieldIndex+=1

		classIndex+=1

	#Extracting info from methods
	index = 0
	for cls in libraryInfo:
		if PRINT: print("Decoding info from methods of: " + cls[0])
		if cls[6] != []: #The class has methods
			methodID = 0
			for method in cls[6]:
				if PRINT: print("*", end = "")
				data = ["", "", "", "", "", "", "", "", []] #Modifier, type, typeInfo, version, info, summary, throws, throwsInfo, vars

				for var in method[3]:
					inputVarInfo = ["", "", ""]
					inputVarInfo[0] = var[0]
					data[8].append(inputVarInfo)

				onInfo = True
				info = ""

				onData = False
				dataType = 0 #1-modifier, 2-type, 3-typeInfo, 4-version, 5-summary, 6-throw, 7-throwInfo, 8-varType, 9-varInfo
				actualData = ""
				inputVarName = ""

				onPossibleData = False
				possibleData = ""
				onPosibleVarName = False
				possibleVarName = ""

				for char in method[4]:
					if char == ':': #Posible data
						if onData:
							if dataType == 1:
								data[0] = actualData.strip()

							elif dataType == 2:
								data[1] = actualData.strip()

							elif dataType == 3:
								data[2] = actualData.strip()

							elif dataType == 4:
								data[3] = actualData.strip()

							elif dataType == 5:
								data[5] = actualData.strip()

							elif dataType == 6:
								data[6] = actualData.strip()

							elif dataType == 7:
								data[7] = actualData.strip()

							elif dataType == 8:
								i = foundVarName(data[8], inputVarName)
								data[8][i][1] = actualData.strip()
								inputVarName = ""

							elif dataType == 9:
								i = foundVarName(data[8], inputVarName)
								data[8][i][2] = actualData.strip()
								inputVarName = ""

							onData = False
							actualData = ""

						if onPossibleData and possibleData != "" and not onPosibleVarName: #We are in method specifications
							if possibleData == "modifier":
								dataType = 1
								onData = True

							elif possibleData == "type":
								dataType = 2
								onData = True

							elif possibleData == "typeInfo":
								dataType = 3
								onData = True

							elif possibleData == "version":
								dataType = 4
								onData = True

							elif possibleData == "summary":
								dataType = 5
								onData = True

							elif possibleData == "throw":
								dataType = 6
								onData = True

							elif possibleData == "throwInfo":
								dataType = 7
								onData = True

							else: #We werent in a specification
								info+=":"+possibleData

							onPossibleData = False
							possibleData = ""

						elif onPossibleData and onPosibleVarName: #We are in var specifications p2
							if possibleData == "type":
								dataType = 8
								onData = True
								inputVarName = possibleVarName.strip()
								possibleVarName = ""

							elif possibleData == "info":
								dataType = 9
								onData = True
								inputVarName = possibleVarName.strip()
								possibleVarName = ""

							else:
								if PRINT: print("Error")

							onPossibleData = False
							onPosibleVarName = False
							possibleData = ""

						else:
							onPossibleData = True

					elif onData:
						actualData+=char

					elif onPossibleData and char != ' ':
						if onPosibleVarName:
							possibleVarName+=char

						else:
							possibleData+=char

					elif onPossibleData and char == ' ': #We are in var specifications p1
						if possibleData == "type" or possibleData == "info":
							onPosibleVarName = True

						else:
							if possibleData == "":
								info+=":"

							else:
								info+=":"+possibleData
							onPossibleData = False

					elif not onPossibleData:
						info+=char

				if onData:
					if dataType == 1:
						data[0] = actualData.strip()

					elif dataType == 2:
						data[1] = actualData.strip()

					elif dataType == 3:
						data[2] = actualData.strip()

					elif dataType == 4:
						data[3] = actualData.strip()

					elif dataType == 5:
						data[5] = actualData.strip()

					elif dataType == 6:
						data[6] = actualData.strip()

					elif dataType == 7:
						data[7] = actualData.strip()

					elif dataType == 8:
						i = foundVarName(data[8], inputVarName)
						data[8][i][1] = actualData.strip()
						inputVarName = ""

					elif dataType == 9:
						i = foundVarName(data[8], inputVarName)
						data[8][i][2] = actualData.strip()
						inputVarName = ""

				if info != "":
					data[4] = info.strip()

				#Adding the extracted data to the general list
				rLibraryInfo[index][6][methodID][0] = data[0]
				rLibraryInfo[index][6][methodID][1] = data[1]
				rLibraryInfo[index][6][methodID][6] = data[2]
				rLibraryInfo[index][6][methodID][5] = data[3]
				rLibraryInfo[index][6][methodID][4] = data[4]
				rLibraryInfo[index][6][methodID][7] = data[5]
				rLibraryInfo[index][6][methodID][8][0] = data[6]
				rLibraryInfo[index][6][methodID][8][1] = data[7]

				for inputVar in data[8]:
					idx = 0
					for iVar in rLibraryInfo[index][6][methodID][3]:
						if str(iVar[0]) == str(inputVar[0]):
							break
						idx+=1
					rLibraryInfo[index][6][methodID][3][idx] = [inputVar[1], inputVar[0], rLibraryInfo[index][6][methodID][3][idx][1], inputVar[2]]

				methodID+=1

		index+=1
		if PRINT: print()

	return rLibraryInfo

def getClasifiedInfo(userInfo, classes):
	def extrendOnIndex(i, toIntroduce, target):
		ri = i
		for x in toIntroduce:
			target.insert(ri, x)
			ri+=1
		return target

	#Errase all unecesary info
	if PRINT: print("Errasing all uneccesary info")

	#Errasing self parameters
	nClasses = classes
	classID = 0
	for cls in classes:
		methodID = 0
		for method in cls[6]:
			try:
				i = method[3].index(SELF_STRUCTURE)
				nClasses[classID][6][methodID][3].pop(i)

			except:
				pass

			methodID+=1

		classID+=1

	classes = nClasses
	if PRINT: print("Errased all uneccesary info")

	if PRINT: print("Organizeing the class heritage...")
	#Setting all direct known subclasses:
	nClasses = classes
	clsID = 0
	for cls in classes:
		for cls2 in classes:
			for super2 in cls2[2]:
				if str(super2) == str(cls[0]):
					nClasses[clsID][7].append(cls2[0])
		clsID+=1
	classes = nClasses

	#Setting all the supers
	names = []
	for cls in classes:
		names.append(cls[0])

	nClasses = classes
	classID = 0
	realSupers = []
	for cls in classes:
		supersNames = []
		superNameID = 0
		supersNames.extend(cls[2])
		realSupers.append(cls[2])
		while True:
			if len(supersNames) <= superNameID: break #There are no more supers
			try:
				i = names.index(supersNames[superNameID])
				supersNames = extrendOnIndex(superNameID+1, classes[i][2], supersNames)

			except ValueError: #If the name is not on the list, it must belong to another class not defined in this package
				if not supersNames[superNameID] in realSupers[classID]:
					supersNames.insert(superNameID+1, supersNames[superNameID])
					superNameID+=1#It has to be done twice to skip the recent added class

			superNameID+=1
		nClasses[classID][2] = supersNames
		classID+=1

	#Deleting the repeated supers from the begining to the end, due to the order of hereditation of python
	classes = nClasses
	classID = 0
	for cls in classes:
		uniqueSupers = []
		supers = []
		for sup in cls[2]:
			supers.append(sup)
		supers.reverse()
		for sup in supers:
			if not sup in uniqueSupers: uniqueSupers.append(sup)
		uniqueSupers.reverse()
		nClasses[classID][2] = uniqueSupers
		classID+=1

	classes = nClasses
	#Setting the super structure as [name, "self/super"] #Depending on if the super is direcly related with the class or not
	clsID = 0
	for cls in classes:
		supID = 0
		for sup in cls[2]:
			if sup in realSupers[clsID]:
				nClasses[clsID][2][supID] = [sup, "self"]
			else:
				nClasses[clsID][2][supID] = [sup, "super"]
			supID+=1
		clsID+=1
	classes = nClasses
	if PRINT: print("Organized the class heritage")

	if PRINT: print("Fixing extra info from methods")
	classIndex = 0
	for cls in classes:
		methodIndex = 0
		for method in cls[6]:
			if method[8] != []:

				#Exceptions
				exceptions = []
				exception = ""
				inList = False
				for char in method[8][0]:
					if char == '[': inList = True
					elif char == ']':
						if exception.strip() != "": exceptions.append(exception.strip())
						exception = ""
						break

					elif char == ',' and inList:
						if exception.strip() != "": exceptions.append(exception.strip())
						exception = ""

					else:
						exception+= char

				if exception.strip() != "": exceptions.append(exception.strip())

				#Exceptions info
				exceptionsInfo = []
				exceptionInfo = ""
				inList = False
				for char in method[8][1]:
					if char == '[': inList = True
					elif char == ']':
						if exceptionInfo.strip() != "": exceptionsInfo.append(exceptionInfo.strip())
						exceptionInfo = ""
						break

					elif char == ',' and inList:
						if exceptionInfo.strip() != "": exceptionsInfo.append(exceptionInfo.strip())
						exceptionInfo = ""

					else:
						exceptionInfo+= char

				if exceptionInfo.strip() != "": exceptionsInfo.append(exceptionInfo.strip())
				if len(exceptions) == len(exceptionsInfo):
					nClasses[classIndex][6][methodIndex][8][0] = exceptions
					nClasses[classIndex][6][methodIndex][8][1] = exceptionsInfo
				else:
					print("In the class: " + cls[0] + " the method: " + method[2] + " has different number of throws and info throws")
					nClasses[classIndex][6][methodIndex][8][0] = []
					nClasses[classIndex][6][methodIndex][8][1] = []

			methodIndex+=1
		classIndex+=1
	classes = nClasses
	if PRINT: print("Fixed extra info from methods")

	#Searching for constructors
	if PRINT: print("Searching for constructors...")
	constructors = []
	for cls in classes:
		if PRINT: print("Class: " + cls[0])
		constructorFound = False
		for method in cls[6]:
			if str(method[2]) == str("__init__"): #It's a constructor
				constructor = method
				constructor[2] = cls[0]
				constructors.append([constructor, "self"])
				constructorFound = True

		if not constructorFound:
			supers = []
			for sup in cls[2]:
				supers.append(sup[0])
			if supers != []:
				for supName in supers:
					try:
						supID = names.index(supName)
						for method in classes[supID][6]:
							if str(method[2]) == str(supName): #It's a constructor
								constructor = method.copy()
								constructor[2] = cls[0]
								constructors.append([constructor, supName])
								constructorFound = True
								break
						if constructorFound: break

					except ValueError: #The class is not defined on the library
						pass

				if not constructorFound:
					constructor = DEFAULT_CONSTRUCTOR
					constructor[2] = cls[0]
					constructors.append([constructor, "default"])

			else: #The function does not have constructors
				constructor = DEFAULT_CONSTRUCTOR
				constructor[2] = cls[0]
				constructors.append([constructor, "default"])

	indx = 0
	for cons in constructors:
		classes[indx][5] = cons
		if cons[1] == "self":
			classes[indx][6].remove(cons[0])
		indx+=1

	if PRINT: print("All constructors found")

	if PRINT: print("Discarding 'NO' classes")
	discardedClasses = []
	for cls in classes:
		if cls[3].lower().strip() == str("no"):
			discardedClasses.append(cls)

	for discardedClass in discardedClasses:
		if PRINT: print(".", end = "")
		classes.remove(discardedClass)
	if PRINT: print()

	if PRINT: print("All 'NO' classes discarded")

	if not userInfo[7]:
		if PRINT: print("Discarding all private methods")
		classIndex = 0
		for cls in classes:
			if PRINT: print(".", end = "")
			privateMethods = []
			for method in cls[6]:
				if method[0].lower() == "private":
					privateMethods.append(method)

			for privateMethod in privateMethods:
				if PRINT: print("*", end = "")
				nClasses[classIndex][6].remove(privateMethod)
			classIndex+=1

		classes = nClasses
		if PRINT: print()
		if PRINT: print("All private methods discarded")

		if PRINT: print("Discarding all private fields")
		classIndex = 0
		for cls in classes:
			if PRINT: print(".", end = "")
			privateFields = []
			for field in cls[4]:
				if field[0].lower() == "private":
					privateFields.append(field)

			for privateField in privateFields:
				if PRINT: print("*", end = "")
				nClasses[classIndex][4].remove(privateField)
			classIndex+=1

		classes = nClasses
		if PRINT: print()
		if PRINT: print("All private fields discarded")

	return classes

def getOrganizedInfo(classes):
	names = []
	for cls in classes:
		names.append(cls[0])

	only = []
	repeated = False
	for name in names:
		if name in only:
			repeated = name
			break

		else: only.append(name)

	if repeated != False:
		print()
		print("Error cant be two classes with the same name, the class name\nthat was found repeated was: " + repeated)
		return False

	repeated = False
	clsR = []
	for cls in classes:
		functNames = []
		for method in cls[6]:
			if not method[2] in functNames: functNames.append(method[2])
			else:
				repeated = method[2]
				break
		if repeated != False:
			clsR = cls[0]
			break
	if repeated != False:
		print()
		print("Error cant be two functions in the same class with the same name, the function name\nthat was found repeated was: " + repeated + ", in the class: " + clsR)
		return False

	#Sorting the classes
	names.sort()
	nClasses = []
	for name in names:
		index = 0
		for cls in classes:
			if str(cls[0]) == str(name):
				break
			index+=1
		nClasses.append(classes[index])
	classes = nClasses

	#Sorting the subs in each class
	for cls in classes:
		cls[7].sort()

	return classes

def generateApi(rute, userInfo, classes):
	names = []
	for cls in classes:
		names.append(cls[0])

	def getInfoWithLinks(info, actualClass):
		linkedText = ""
		idx = 0
		inLink = False
		link = ""
		inParenthesis = ""
		pattern = re.compile(r"((https?|ftp)\:\/\/([\w-]+\.)?([\w-])+\.(\w)+\/?[\w\?\.\=\&\-\#\+\/]+)")
		skipNext = False
		for char in info:
			if skipNext:
				skipNext = False
				continue

			if char == '{': #Could be a link
				if idx > 1 and info[idx-1] == ')':
					parenthesisFound = False
					for char2 in info[0:idx-1][::-1]:
						if char2 == '(':
							parenthesisFound = True
							break
						else: inParenthesis+=char2
					if parenthesisFound: inLink = True
					inParenthesis = inParenthesis[::-1]
				else: linkedText+=char

			elif inLink and char == '}':
				match = pattern.match(link)
				linkedText = linkedText.rstrip('('+inParenthesis+')')
				if match != None: #It is a https link or similar
					typ = info[idx+1]
					if typ == 's':
						linkedText+=INFO_WEB_LINK_S.format(match.group(0), inParenthesis)
						skipNext = True
						idx+=1

					elif typ == 'o':
						linkedText+=INFO_WEB_LINK_O.format(match.group(0), inParenthesis)
						skipNext = True
						idx+=1

					elif typ == 'p':
						linkedText+=INFO_WEB_LINK_P.format(match.group(0), inParenthesis)
						skipNext = True
						idx+=1

					elif typ == 'v':
						linkedText+=INFO_WEB_LINK_V.format(match.group(0), inParenthesis)
						skipNext = True
						idx+=1

					else: linkedText+=INFO_WEB_LINK_O.format(match.group(0), inParenthesis)

				else:
					try:
						i = names.index(link)
						cls = classes[i]
						linkedText+=INFO_API_LINK.format(link, cls[1], inParenthesis)
					except: #I the link is not a url or a class of this library, the link will be discarded
						try:
							methodNames = []
							for method in actualClass[6]:
								methodNames.append(method[2])

							i = methodNames.index(link)
							method = actualClass[6][i]
							linkedText+=INFO_API_METHOD_LINK.format(actualClass[0], method[2])
						except:
							try:
								fieldNames = []
								for field in actualClass[6]:
									fieldNames.append(field[2])

								i = fieldNames.index(link)
								field = actualClass[6][i]
								linkedText+=INFO_API_FIELD_LINK.format(actualClass[0], field[2])

							except:
								linkedText+=inParenthesis
				link = ""
				inParenthesis = ""
				inLink = False

			elif not inLink:
				linkedText+=char

			elif inLink:
				link+=char

			idx+=1

		return linkedText

	#AllClasses_Frame generator
	allClasses_Frame = open(rute + "allclasses-frame.html", "w")
	program_head = PROGRAM_HEAD.format(userInfo[5], datetime.now(), "All Classes")
	allClasses_Frame.write(program_head)
	allClasses_Frame.write(ALL_CLASSES_MAIN.format(datetime.now().strftime("%Y-%m-%d")))
	for cls in classes:
		allClasses_Frame.write(CLASS.format(cls[0], cls[1]))

	allClasses_Frame.write(ALL_CLASSES_END)
	allClasses_Frame.close()

	#Class by class generator
	for cls in classes:

		#Opening file
		actualClass = open(rute + "{0}.html".format(cls[0]), "w")
		program_head = PROGRAM_HEAD.format(userInfo[5], datetime.now(), cls[0])

		#Head
		actualClass.write(program_head)
		actualClass.write('<meta name="date" content="{0}">'.format(datetime.now().strftime("%Y-%m-%d")))
		actualClass.write(CLASS_0)
		actualClass.write("parent.document.title="+ cls[0] +";}")
		actualClass.write(CLASS_0_1.format(userInfo[1], cls[0]))

		#Supers extraction
		supers = cls[2]
		try:
			supers.reverse()
		except:
			pass

		#Supers in html
		for supComp in supers:
			try:
				i = names.index(supComp[0])
				sup = classes[i]
			except:
				sup = [supComp[0], "NoInfo." + supComp[0]]

			dot = False
			dir = sup[1]
			for char in sup[1][::-1]:
				if char == '.':
					dot = True
				dir[:len(dir) - 1]
				if dot: break

			actualClass.write(CLASS_1.format(sup[0], dir, sup[1]))
		actualClass.write(CLASS_2.format(cls[1]))
		for sup in cls[2]:
			actualClass.write("\n</li>\n</ul>")

		#Subclasses
		actualClass.write('\n<div class="description">\n<ul class="blockList">\n<li class="blockList">')
		first = True
		subclasses = False
		for subName in cls[7]: #To implement
			subclasses = True
			try:
				i = names.index(subName)
				sub = classes[i]
			except:
				sub = [subName, "NoInfo." + subName]
			if first:
				actualClass.write("\n<dl>\n<dt>Direct Known Subclasses:</dt>\n<dd>")
				actualClass.write(CLASS_3.format(sub[0], sub[1]))
			else: actualClass.write(CLASS_3_1.format(sub[0], sub[1]))
			first = False
		if subclasses: actualClass.write("\n</dd>\n</dl>")

		#Init Info
		actualClass.write(CLASS_4.format(cls[0]))
		first = True
		for supComp in cls[2]:
			if supComp[1] == "self":
				try:
					i = names.index(supComp[0])
					sup = classes[i]
					if first:
						actualClass.write("\nextends ")
						actualClass.write(CLASS_5.format(sup[0], sup[1]))

					else: actualClass.write(CLASS_5_1.format(sup[0], sup[1]))
					first = False
				except:
					pass
		actualClass.write("</pre>")
		actualClass.write('\n<div class="block">')
		actualClass.write(getInfoWithLinks(cls[3].strip(), cls))
		actualClass.write("</div>\n</li>\n</ul>\n</div>")

		#Summary
		actualClass.write(SUMMARY_1)

		#Field summary
		hasFieldsInSupers = False
		for supComp in cls[2]:
			try:
				i = names.index(supComp[0])
				sup = classes[i]
				if sup[4] != []: hasFieldsInSupers = True
			except:
				pass
		if cls[4] != [] or hasFieldsInSupers: actualClass.write(FIELD_SUMMARY_1)
		if cls[4] != []: actualClass.write(FIELD_SUMMARY_1_2)
		altColor = True
		isList = False
		for field in cls[4]:

			#Background color
			if altColor:
				altColor = False
				actualClass.write(ALT_COLOR) #Background color 1
			else:
				altColor = True
				actualClass.write(ROW_COLOR) #Background color 2

			#Modifier, type and name of the field
			mod = field[0].lower()
			typ = field[1]
			if typ == "": typ = "void"
			if typ.lower() == "void": typ = typ.lower()
			if mod == "": mod = "public"
			if typ.startswith("[") and typ.endswith("]"): #It's a list
				typ = typ.lstrip('[')
				typ = typ.rstrip(']')
				if typ in names:
					i = names.index(typ)
					dir = classes[i]
					actualClass.write(FIELD_SUMMARY_2_1_p.format(cls[0], field[2], mod, dir[0], dir[1]))

				else:
					actualClass.write(FIELD_SUMMARY_2_p.format(cls[0], field[2], mod, typ))

			else:
				if typ in names:
					i = names.index(typ)
					dir = classes[i]
					actualClass.write(FIELD_SUMMARY_2_1.format(cls[0], field[2], mod, dir[0], dir[1]))

				else:
					actualClass.write(FIELD_SUMMARY_2.format(cls[0], field[2], mod, typ))
			actualClass.write(FIELD_SUMMARY_3.format(getInfoWithLinks(field[4], cls))) #)\n info
		if cls[4] != []: actualClass.write("</table>") #Table end
		for supComp in supers:
			try:
				i = names.index(supComp[0])
				sup = classes[i]
			except:
				sup = [supComp[0], "NoInfo." + supComp[0], "", "", []]

			if sup[4] != []: actualClass.write(FIELDS_INHERITED_1.format(sup[1].lstrip('.'+sup[0]), sup[0]))
			first = True
			for field in sup[4]:
				if first:
					actualClass.write(FIELDS_INHERITED_2.format(sup[0], field[2]))
					first = False
				else:
					actualClass.write(FIELDS_INHERITED_2_1.format(sup[0], field[2]))
			if sup[4] != []: actualClass.write("</code></li>\n</ul>")
		if cls[4] != [] or hasFieldsInSupers: actualClass.write("\n</li>\n</ul>")

		#Constructor summary
		if cls[5][1] != "self" and cls[5][1] != "default": actualClass.write(CONSTRUCTOR_SUMMARY_1.format(CONSTRUCTOR_SUMMARY_1_bis.format(cls[5][1])))
		else: actualClass.write(CONSTRUCTOR_SUMMARY_1.format(""))
		actualClass.write(CONSTRUCTOR_SUMMARY_2.format(cls[0]))
		first = True
		notInClass = False
		isList = False
		for var in cls[5][0][3]:

			if var[0].startswith("[") and var[0].endswith("]"): #It's a list
				isList = True
				var[0] = var[0].lstrip('[')
				var[0] = var[0].rstrip(']')

			if var[0] in names and var[0].strip() != "": #The type is defined in this library
				i = names.index(var[0])
				dir = classes[i]

			else:
				notInClass = True
				dir = ["NotDefined", var[1]]
				if var[0].strip() != "":
					dir = [var[0], var[1]]

			if isList:
				if first:
					if notInClass: actualClass.write(CONSTRUCTOR_SUMMARY_3_1_p.format(dir[0], dir[1]))
					else: actualClass.write(CONSTRUCTOR_SUMMARY_3_p.format(dir[0], dir[1], var[1]))

				else:
					if notInClass: actualClass.write(CONSTRUCTOR_SUMMARY_4_1_p.format(dir[0], dir[1]))
					else: actualClass.write(CONSTRUCTOR_SUMMARY_4_p.format(dir[0], dir[1], var[1]))
				var[0] = '['+var[0]+']'

			else:
				if first:
					if notInClass: actualClass.write(CONSTRUCTOR_SUMMARY_3_1.format(dir[0], dir[1]))
					else: actualClass.write(CONSTRUCTOR_SUMMARY_3.format(dir[0], dir[1], var[1]))

				else:
					if notInClass: actualClass.write(CONSTRUCTOR_SUMMARY_4_1.format(dir[0], dir[1]))
					else: actualClass.write(CONSTRUCTOR_SUMMARY_4.format(dir[0], dir[1], var[1]))

			first = False
			notInClass = False
			isList = False
		actualClass.write(CONSTRUCTOR_SUMMARY_5.format(getInfoWithLinks(cls[5][0][7], cls)))
		actualClass.write("\n</table>\n</li>\n</ul>")

		#Method summary
		if cls[6] != []: actualClass.write(METHOD_SUMMARY_1) #Table creation
		altColor = True
		isList = False
		for method in cls[6]:

			#Background color
			if altColor:
				altColor = False
				actualClass.write(ALT_COLOR) #Background color 1
			else:
				altColor = True
				actualClass.write(ROW_COLOR) #Background color 2

			#Modifier, type and name of the method
			mod = method[0].lower()
			typ = method[1]
			if typ == "": typ = "void"
			if typ.lower() == "void": typ = typ.lower()
			if mod == "": mod = "public"
			if typ.startswith("[") and typ.endswith("]"): #It's a list
				typ = typ.lstrip('[')
				typ = typ.rstrip(']')
				if typ in names:
					i = names.index(typ)
					dir = classes[i]
					actualClass.write(METHOD_SUMMARY_2_1_p.format(cls[0], method[2], mod, dir[0], dir[1]))

				else:
					actualClass.write(METHOD_SUMMARY_2_p.format(cls[0], method[2], mod, typ))

			else:
				if typ in names:
					i = names.index(typ)
					dir = classes[i]
					actualClass.write(METHOD_SUMMARY_2_1.format(cls[0], method[2], mod, dir[0], dir[1]))

				else:
					actualClass.write(METHOD_SUMMARY_2.format(cls[0], method[2], mod, typ))

			first = True
			isList = False
			notInClass = False

			#Vars of the method
			for var in method[3]:

				if var[0].startswith("[") and var[0].endswith("]"): #It's a list
					isList = True
					var[0] = var[0].lstrip('[')
					var[0] = var[0].rstrip(']')

				if var[0] in names and var[0].strip() != "": #The type is defined in this library
					i = names.index(var[0])
					dir = classes[i]

				else:
					notInClass = True
					dir = ["NotDefined", var[1]]
					if var[0].strip() != "":
						dir = [var[0], var[1]]

				if isList:
					if first:
						if notInClass: actualClass.write(METHOD_SUMMARY_3_1_p.format(dir[0], dir[1]))
						else: actualClass.write(METHOD_SUMMARY_3_p.format(dir[0], dir[1], var[1]))

					else:
						if notInClass: actualClass.write(METHOD_SUMMARY_4_1_p.format(dir[0], dir[1]))
						else: actualClass.write(METHOD_SUMMARY_4_p.format(dir[0], dir[1], var[1]))
					var[0] = '['+var[0]+']'

				else:
					if first:
						if notInClass: actualClass.write(METHOD_SUMMARY_3_1.format(dir[0], dir[1]))
						else: actualClass.write(METHOD_SUMMARY_3.format(dir[0], dir[1], var[1]))

					else:
						if notInClass: actualClass.write(METHOD_SUMMARY_4_1.format(dir[0], dir[1]))
						else: actualClass.write(METHOD_SUMMARY_4.format(dir[0], dir[1], var[1]))

				first = False
				notInClass = False
				isList = False

			actualClass.write(METHOD_SUMMARY_5.format(getInfoWithLinks(method[7], cls))) #)\n info
		if cls[6] != []: actualClass.write("</table>") #Table end
		for supComp in supers:
			try:
				i = names.index(supComp[0])
				sup = classes[i]
			except:
				sup = [supComp[0], "NoInfo." + supComp[0], "", "", [], "", []]

			if sup[6] != []: actualClass.write(METHODS_INHERITED_1.format(sup[1].lstrip('.'+sup[0]), sup[0]))
			first = True
			for method in sup[6]:
				repeated = False
				for methodS in cls[6]:
					if method[2] == methodS[2]: repeated = True

				if not repeated:
					if first:
						actualClass.write(METHODS_INHERITED_2.format(sup[0], method[2]))
						first = False
					else:
						actualClass.write(METHODS_INHERITED_2_1.format(sup[0], method[2]))
			if sup[6] != []: actualClass.write("</code></li>\n</ul>")
		if cls[6] != []: actualClass.write("\n</li>\n</ul>\n</li>\n</ul>")

		#End summary
		actualClass.write("\n</div>")

		#Details
		actualClass.write(DETAILS_1)

		#Fields detail
		if cls[4] != []: actualClass.write(FIELD_DETAIL_1)
		for field in cls[4]:
			actualClass.write(FIELD_DETAIL_2.format(field[2]))

			mod = field[0].lower()
			typ = field[1]
			if typ == "": typ = "void"
			if typ.lower() == "void": typ = typ.lower()
			if mod == "": mod = "public"
			if typ.startswith("[") and typ.endswith("]"): #It's a list
				typ = typ.lstrip('[')
				typ = typ.rstrip(']')
				if typ in names:
					i = names.index(typ)
					dir = classes[i]
					actualClass.write(FIELD_DETAIL_3_2_p.format(field[2], mod, dir[0], dir[1], getInfoWithLinks(field[4], cls)))

				else:
					actualClass.write(FIELD_DETAIL_3_1_p.format(field[2], mod, typ, getInfoWithLinks(field[4], cls)))

			else:
				if typ in names:
					i = names.index(typ)
					dir = classes[i]
					actualClass.write(FIELD_DETAIL_3_2.format(field[2], mod, dir[0], dir[1], getInfoWithLinks(field[4], cls)))

				else:
					actualClass.write(FIELD_DETAIL_3_1.format(field[2], mod, typ, getInfoWithLinks(field[4], cls)))
		if cls[4] != []: actualClass.write("\n</li>\n</ul>")

		#Constructor details
		if cls[5] != "": actualClass.write(CONSTRUCTOR_DETAIL_1)
		first = True
		notInClass = False
		isList = False
		compound = ""
		for var in cls[5][0][3]:
			if var[0].startswith("[") and var[0].endswith("]"): #It's a list
				isList = True
				var[0] = var[0].lstrip('[')
				var[0] = var[0].rstrip(']')

			if var[0] in names and var[0].strip() != "": #The type is defined in this library
				i = names.index(var[0])
				dir = classes[i]

			else:
				notInClass = True
				dir = ["NotDefined", var[1]]
				if var[0].strip() != "":
					dir = [var[0], var[1]]

			if isList:
				if first:
					if notInClass: compound+=CONSTRUCTOR_SUMMARY_3_1_p.format(dir[0], dir[1])
					else: compound+=CONSTRUCTOR_SUMMARY_3_p.format(dir[0], dir[1], var[1])

				else:
					if notInClass: compound+="\n\t"+CONSTRUCTOR_SUMMARY_4_1_p.format(dir[0], dir[1])
					else: compound+="\n\t"+CONSTRUCTOR_SUMMARY_4_p.format(dir[0], dir[1], var[1])
				var[0] = '['+var[0]+']'

			else:
				if first:
					if notInClass: compound+=CONSTRUCTOR_SUMMARY_3_1.format(dir[0], dir[1])
					else: compound+=CONSTRUCTOR_SUMMARY_3.format(dir[0], dir[1], var[1])

				else:
					if notInClass: compound+="\n\t"+CONSTRUCTOR_SUMMARY_4_1.format(dir[0], dir[1])
					else: compound+="\n\t"+CONSTRUCTOR_SUMMARY_4.format(dir[0], dir[1], var[1])

			if var[2] != "": compound+=" = " + var[2]
			first = False
			notInClass = False
			isList = False

		if cls[5] != "": actualClass.write(CONSTRUCTOR_DETAIL_2.format(cls[5][0][2], compound, getInfoWithLinks(cls[5][0][4], cls)))

		#Extra info
		if cls[5][0][3] != [] or cls[5][0][5] != "" or cls[5][0][6] != "" or cls[5][0][8][0] != []: actualClass.write("<dl>")

		#Returns
		if cls[5][0][6] != "": actualClass.write('<dt><span class="strong">Returns:</span></dt><dd>{0}</dd>'.format(getInfoWithLinks(cls[5][0][6], cls)))

		#Overrides
		repeated = False
		for supComp in supers:
			try:
				i = names.index(supComp[0])
				sup = classes[i]
				for methodS in sup[6]:
					if cls[5][0][2] == methodS[2]: repeated = sup
			except:
				pass
		if repeated != False:
			actualClass.write('<dt><strong>Overrides:</strong></dt><dd><code><a href="{0}.html#{2}">{2}</a></code>&nbsp;in class&nbsp;<code><a href="{0}.html" title="class in {1}">{0}</a></code></dd>'.format(repeated[0], repeated[1], cls[5][0][2]))

		#Parameters
		if cls[5][0][3] != []: actualClass.write(METHOD_DETAIL_PARAMETRES_1)
		for parameter in cls[5][0][3]:
			if parameter[3] == "": parameterInfo = "No info disponible"
			else: parameterInfo = parameter[3]
			actualClass.write(METHOD_DETAIL_PARAMETRES_2.format(parameter[1], getInfoWithLinks(parameterInfo, cls)))

		#Throws
		if cls[0] == "Component": print(cls[5][0][8])
		if cls[5][0][8] != [[], []]: actualClass.write(METHOD_DETAIL_THROWS_1)
		throwIndex = 0
		for throw in cls[5][0][8][0]:
			if throw in names:
				i = names.index(throw)
				dir = classes[i]
				actualClass.write(METHOD_DETAIL_THROWS_2_1.format(dir[0], dir[1], getInfoWithLinks(cls[5][0][8][1][throwIndex], cls)))
			else: actualClass.write(METHOD_DETAIL_THROWS_2_2.format(throw, getInfoWithLinks(cls[5][0][8][1][throwIndex], cls)))
			throwIndex+=1

		#Version
		if cls[5][0][5] != "": actualClass.write('<dt><span class="strong">Since:</span></dt>\n<dd>{0}</dd>'.format(cls[5][0][5]))
		
		#End of extra info
		if cls[5][0][3] != [] or cls[5][0][5] != "" or cls[5][0][6] != "" or cls[5][0][8][0] != []: actualClass.write("</dl>")
		
		actualClass.write("\n</li>\n</ul>\n</li>\n</ul>")

		#Method details
		if cls[6] != []: actualClass.write(METHOD_DETAIL_1)
		for method in cls[6]:

			actualClass.write(METHOD_DETAIL_2.format(method[2]))

			#Modifier, type and name of the method
			mod = method[0].lower()
			typ = method[1]
			if typ == "": typ = "void"
			if typ.lower() == "void": typ = typ.lower()
			if mod == "": mod = "public"
			if typ.startswith("[") and typ.endswith("]"): #It's a list
				typ = typ.lstrip('[')
				typ = typ.rstrip(']')
				if typ in names:
					i = names.index(typ)
					dir = classes[i]
					actualClass.write(METHOD_DETAIL_3_2_p.format(mod, dir[0], dir[1], method[2]))

				else:
					actualClass.write(METHOD_DETAIL_3_1_p.format(mod, typ, method[2]))

			else:
				if typ in names:
					i = names.index(typ)
					dir = classes[i]
					actualClass.write(METHOD_DETAIL_3_2.format(mod, dir[0], dir[1], method[2]))

				else:
					actualClass.write(METHOD_DETAIL_3_1.format(mod, typ, method[2]))

			first = True
			isList = False
			notInClass = False
			compound = ""
			#Vars of the method
			for var in method[3]:

				if var[0].startswith("[") and var[0].endswith("]"): #It's a list
					isList = True
					var[0] = var[0].lstrip('[')
					var[0] = var[0].rstrip(']')

				if var[0] in names and var[0].strip() != "": #The type is defined in this library
					i = names.index(var[0])
					dir = classes[i]

				else:
					notInClass = True
					dir = ["NotDefined", var[1]]
					if var[0].strip() != "":
						dir = [var[0], var[1]]

				if isList:
					if first:
						if notInClass: compound+=METHOD_SUMMARY_3_1_p.format(dir[0], dir[1])
						else: compound+=METHOD_SUMMARY_3_p.format(dir[0], dir[1], var[1])

					else:
						if notInClass: compound+="\n\t"+METHOD_SUMMARY_4_1_p.format(dir[0], dir[1])
						else: compound+="\n\t"+METHOD_SUMMARY_4_p.format(dir[0], dir[1], var[1])
					var[0] = '['+var[0]+']'

				else:
					if first:
						if notInClass: compound+=METHOD_SUMMARY_3_1.format(dir[0], dir[1])
						else: compound+=METHOD_SUMMARY_3.format(dir[0], dir[1], var[1])

					else:
						if notInClass: compound+="\n\t"+METHOD_SUMMARY_4_1.format(dir[0], dir[1])
						else: compound+="\n\t"+METHOD_SUMMARY_4.format(dir[0], dir[1], var[1])

				if var[2] != "": compound+=" = " + var[2]

				first = False
				notInClass = False
				isList = False

			actualClass.write(METHOD_DETAIL_4.format(compound, getInfoWithLinks(method[4], cls)))

			#Extra info
			if method[3] != [] or method[5] != "" or method[6] != "" or method[8][0] != []: actualClass.write("<dl>")

			#Returns
			if method[6] != "": actualClass.write('<dt><span class="strong">Returns:</span></dt><dd>{0}</dd>'.format(getInfoWithLinks(method[6], cls)))

			#Overrides
			repeated = False
			for supComp in supers:
				try:
					i = names.index(supComp[0])
					sup = classes[i]
					for methodS in sup[6]:
						if method[2] == methodS[2]: repeated = sup
				except:
					pass
			if repeated != False:
				actualClass.write('<dt><strong>Overrides:</strong></dt><dd><code><a href="{0}.html#{2}">{2}</a></code>&nbsp;in class&nbsp;<code><a href="{0}.html" title="class in {1}">{0}</a></code></dd>'.format(repeated[0], repeated[1], method[2]))

			#Parameters
			if method[3] != []: actualClass.write(METHOD_DETAIL_PARAMETRES_1)
			for parameter in method[3]:
				if parameter[3] == "": parameterInfo = "No info disponible"
				else: parameterInfo = parameter[3]
				actualClass.write(METHOD_DETAIL_PARAMETRES_2.format(parameter[1], getInfoWithLinks(parameterInfo, cls)))

			#Throws
			if method[8] != [[], []]: actualClass.write(METHOD_DETAIL_THROWS_1)
			throwIndex = 0
			for throw in method[8][0]:
				if throw in names:
					i = names.index(throw)
					dir = classes[i]
					actualClass.write(METHOD_DETAIL_THROWS_2_1.format(dir[0], dir[1], getInfoWithLinks(method[8][1][throwIndex], cls)))
				else: actualClass.write(METHOD_DETAIL_THROWS_2_2.format(throw, getInfoWithLinks(method[8][1][throwIndex], cls)))
				throwIndex+=1

			#Version
			if method[5] != "": actualClass.write('<dt><span class="strong">Since:</span></dt>\n<dd>{0}</dd>'.format(method[5]))
			
			#End of extra info
			if method[3] != [] or method[5] != "" or method[6] != "" or method[8][0] != []: actualClass.write("</dl>")
			actualClass.write("\n</li>\n</ul>")
		if cls[6] != []: actualClass.write("\n</li>\n</ul>")

		#End details
		actualClass.write("\n</li>\n</ul>\n</div>")

		#Info of the class
		actualClass.write("\n</div>\n</body>\n</html>")
		actualClass.close()

if __name__ == '__main__':
	main()
