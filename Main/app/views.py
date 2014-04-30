




<!DOCTYPE html>
<html class="   ">
  <head prefix="og: http://ogp.me/ns# fb: http://ogp.me/ns/fb# object: http://ogp.me/ns/object# article: http://ogp.me/ns/article# profile: http://ogp.me/ns/profile#">
    <meta charset='utf-8'>
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    
    
    <title>GetARoom/Main/app/views.py at master · dimitdim/GetARoom</title>
    <link rel="search" type="application/opensearchdescription+xml" href="/opensearch.xml" title="GitHub" />
    <link rel="fluid-icon" href="https://github.com/fluidicon.png" title="GitHub" />
    <link rel="apple-touch-icon" sizes="57x57" href="/apple-touch-icon-114.png" />
    <link rel="apple-touch-icon" sizes="114x114" href="/apple-touch-icon-114.png" />
    <link rel="apple-touch-icon" sizes="72x72" href="/apple-touch-icon-144.png" />
    <link rel="apple-touch-icon" sizes="144x144" href="/apple-touch-icon-144.png" />
    <meta property="fb:app_id" content="1401488693436528"/>

      <meta content="@github" name="twitter:site" /><meta content="summary" name="twitter:card" /><meta content="dimitdim/GetARoom" name="twitter:title" /><meta content="Contribute to GetARoom development by creating an account on GitHub." name="twitter:description" /><meta content="https://avatars3.githubusercontent.com/u/5540901?s=400" name="twitter:image:src" />
<meta content="GitHub" property="og:site_name" /><meta content="object" property="og:type" /><meta content="https://avatars3.githubusercontent.com/u/5540901?s=400" property="og:image" /><meta content="dimitdim/GetARoom" property="og:title" /><meta content="https://github.com/dimitdim/GetARoom" property="og:url" /><meta content="Contribute to GetARoom development by creating an account on GitHub." property="og:description" />

    <link rel="assets" href="https://github.global.ssl.fastly.net/">
    <link rel="conduit-xhr" href="https://ghconduit.com:25035/">
    <link rel="xhr-socket" href="/_sockets" />

    <meta name="msapplication-TileImage" content="/windows-tile.png" />
    <meta name="msapplication-TileColor" content="#ffffff" />
    <meta name="selected-link" value="repo_source" data-pjax-transient />
    <meta content="collector.githubapp.com" name="octolytics-host" /><meta content="collector-cdn.github.com" name="octolytics-script-host" /><meta content="github" name="octolytics-app-id" /><meta content="D05B37AD:3E22:1E4986:536184C5" name="octolytics-dimension-request_id" /><meta content="5540901" name="octolytics-actor-id" /><meta content="dimitdim" name="octolytics-actor-login" /><meta content="2e3e30026aee727b060497d097e2a3fc90eb8723c0debe3d7fc03e90035498d6" name="octolytics-actor-hash" />
    

    
    
    <link rel="icon" type="image/x-icon" href="https://github.global.ssl.fastly.net/favicon.ico" />

    <meta content="authenticity_token" name="csrf-param" />
<meta content="ZeB6upeVX6Lot+ddxj9CGXBrYEELk1M/gUB6W8EEmVmw5jBoUfTQQduKkuuinNr5HNFfUJhQAuXTZE1cyu0uwA==" name="csrf-token" />

    <link href="https://github.global.ssl.fastly.net/assets/github-f0895a81be130c641ffd020be9a12dd2e72a41ee.css" media="all" rel="stylesheet" type="text/css" />
    <link href="https://github.global.ssl.fastly.net/assets/github2-dcb74cba8c44bd3e3ec7929782122624f01d0536.css" media="all" rel="stylesheet" type="text/css" />
    


        <script crossorigin="anonymous" src="https://github.global.ssl.fastly.net/assets/frameworks-abc81e706df1b74d6ac26c344580917e7afe15bb.js" type="text/javascript"></script>
        <script async="async" crossorigin="anonymous" src="https://github.global.ssl.fastly.net/assets/github-9b7e53007ac295d4c0a9432530541a4c5101c287.js" type="text/javascript"></script>
        
        
      <meta http-equiv="x-pjax-version" content="fd6f3a72bef9f297131bde02fe31b0af">

      
  <meta name="description" content="Contribute to GetARoom development by creating an account on GitHub." />

  <meta content="5540901" name="octolytics-dimension-user_id" /><meta content="dimitdim" name="octolytics-dimension-user_login" /><meta content="18165411" name="octolytics-dimension-repository_id" /><meta content="dimitdim/GetARoom" name="octolytics-dimension-repository_nwo" /><meta content="true" name="octolytics-dimension-repository_public" /><meta content="false" name="octolytics-dimension-repository_is_fork" /><meta content="18165411" name="octolytics-dimension-repository_network_root_id" /><meta content="dimitdim/GetARoom" name="octolytics-dimension-repository_network_root_nwo" />
  <link href="https://github.com/dimitdim/GetARoom/commits/master.atom" rel="alternate" title="Recent Commits to GetARoom:master" type="application/atom+xml" />

  </head>


  <body class="logged_in  env-production windows vis-public page-blob">
    <a href="#start-of-content" tabindex="1" class="accessibility-aid js-skip-to-content">Skip to content</a>
    <div class="wrapper">
      
      
      
      


      <div class="header header-logged-in true">
  <div class="container clearfix">

    <a class="header-logo-invertocat" href="https://github.com/">
  <span class="mega-octicon octicon-mark-github"></span>
</a>

    
    <a href="/notifications" aria-label="You have no unread notifications" class="notification-indicator tooltipped tooltipped-s" data-hotkey="g n">
        <span class="mail-status all-read"></span>
</a>

      <div class="command-bar js-command-bar  in-repository">
          <form accept-charset="UTF-8" action="/search" class="command-bar-form" id="top_search_form" method="get">

<div class="commandbar">
  <span class="message"></span>
  <input type="text" data-hotkey="s, /" name="q" id="js-command-bar-field" placeholder="Search or type a command" tabindex="1" autocapitalize="off"
    
    data-username="dimitdim"
      data-repo="dimitdim/GetARoom"
      data-branch="master"
      data-sha="b771d3c29623db85c60940bc774dee80417a06e9"
  >
  <div class="display hidden"></div>
</div>

    <input type="hidden" name="nwo" value="dimitdim/GetARoom" />

    <div class="select-menu js-menu-container js-select-menu search-context-select-menu">
      <span class="minibutton select-menu-button js-menu-target" role="button" aria-haspopup="true">
        <span class="js-select-button">This repository</span>
      </span>

      <div class="select-menu-modal-holder js-menu-content js-navigation-container" aria-hidden="true">
        <div class="select-menu-modal">

          <div class="select-menu-item js-navigation-item js-this-repository-navigation-item selected">
            <span class="select-menu-item-icon octicon octicon-check"></span>
            <input type="radio" class="js-search-this-repository" name="search_target" value="repository" checked="checked" />
            <div class="select-menu-item-text js-select-button-text">This repository</div>
          </div> <!-- /.select-menu-item -->

          <div class="select-menu-item js-navigation-item js-all-repositories-navigation-item">
            <span class="select-menu-item-icon octicon octicon-check"></span>
            <input type="radio" name="search_target" value="global" />
            <div class="select-menu-item-text js-select-button-text">All repositories</div>
          </div> <!-- /.select-menu-item -->

        </div>
      </div>
    </div>

  <span class="help tooltipped tooltipped-s" aria-label="Show command bar help">
    <span class="octicon octicon-question"></span>
  </span>


  <input type="hidden" name="ref" value="cmdform">

</form>
        <ul class="top-nav">
          <li class="explore"><a href="/explore">Explore</a></li>
            <li><a href="https://gist.github.com">Gist</a></li>
            <li><a href="/blog">Blog</a></li>
          <li><a href="https://help.github.com">Help</a></li>
        </ul>
      </div>

    


  <ul id="user-links">
    <li>
      <a href="/dimitdim" class="name">
        <img alt="Dimitar Dimitrov" class=" js-avatar" data-user="5540901" height="20" src="https://avatars0.githubusercontent.com/u/5540901?s=140" width="20" /> dimitdim
      </a>
    </li>

    <li class="new-menu dropdown-toggle js-menu-container">
      <a href="#" class="js-menu-target tooltipped tooltipped-s" aria-label="Create new...">
        <span class="octicon octicon-plus"></span>
        <span class="dropdown-arrow"></span>
      </a>

      <div class="new-menu-content js-menu-content">
      </div>
    </li>

    <li>
      <a href="/settings/profile" id="account_settings"
        class="tooltipped tooltipped-s"
        aria-label="Account settings ">
        <span class="octicon octicon-tools"></span>
      </a>
    </li>
    <li>
      <form class="logout-form" action="/logout" method="post">
        <button class="sign-out-button tooltipped tooltipped-s" aria-label="Sign out">
          <span class="octicon octicon-log-out"></span>
        </button>
      </form>
    </li>

  </ul>

<div class="js-new-dropdown-contents hidden">
  

<ul class="dropdown-menu">
  <li>
    <a href="/new"><span class="octicon octicon-repo-create"></span> New repository</a>
  </li>
  <li>
    <a href="/organizations/new"><span class="octicon octicon-organization"></span> New organization</a>
  </li>


    <li class="section-title">
      <span title="dimitdim/GetARoom">This repository</span>
    </li>
      <li>
        <a href="/dimitdim/GetARoom/issues/new"><span class="octicon octicon-issue-opened"></span> New issue</a>
      </li>
      <li>
        <a href="/dimitdim/GetARoom/settings/collaboration"><span class="octicon octicon-person-add"></span> New collaborator</a>
      </li>
</ul>

</div>


    
  </div>
</div>

      

        



      <div id="start-of-content" class="accessibility-aid"></div>
          <div class="site" itemscope itemtype="http://schema.org/WebPage">
    <div id="js-flash-container">
      
    </div>
    <div class="pagehead repohead instapaper_ignore readability-menu">
      <div class="container">
        

<ul class="pagehead-actions">

    <li class="subscription">
      <form accept-charset="UTF-8" action="/notifications/subscribe" class="js-social-container" data-autosubmit="true" data-remote="true" method="post"><div style="margin:0;padding:0;display:inline"><input name="authenticity_token" type="hidden" value="axJ/XbGV/dvZ2mBDtYqI+5kger40uRBnOgJTaB8/5xbuZyofl7ewSa/gJw9Yxd0brWyeM1iUUVi7+4ZUnASrug==" /></div>  <input id="repository_id" name="repository_id" type="hidden" value="18165411" />

    <div class="select-menu js-menu-container js-select-menu">
      <a class="social-count js-social-count" href="/dimitdim/GetARoom/watchers">
        3
      </a>
      <span class="minibutton select-menu-button with-count js-menu-target" role="button" tabindex="0" aria-haspopup="true">
        <span class="js-select-button">
          <span class="octicon octicon-eye-unwatch"></span>
          Unwatch
        </span>
      </span>

      <div class="select-menu-modal-holder">
        <div class="select-menu-modal subscription-menu-modal js-menu-content" aria-hidden="true">
          <div class="select-menu-header">
            <span class="select-menu-title">Notification status</span>
            <span class="octicon octicon-remove-close js-menu-close"></span>
          </div> <!-- /.select-menu-header -->

          <div class="select-menu-list js-navigation-container" role="menu">

            <div class="select-menu-item js-navigation-item " role="menuitem" tabindex="0">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <div class="select-menu-item-text">
                <input id="do_included" name="do" type="radio" value="included" />
                <h4>Not watching</h4>
                <span class="description">You only receive notifications for conversations in which you participate or are @mentioned.</span>
                <span class="js-select-button-text hidden-select-button-text">
                  <span class="octicon octicon-eye-watch"></span>
                  Watch
                </span>
              </div>
            </div> <!-- /.select-menu-item -->

            <div class="select-menu-item js-navigation-item selected" role="menuitem" tabindex="0">
              <span class="select-menu-item-icon octicon octicon octicon-check"></span>
              <div class="select-menu-item-text">
                <input checked="checked" id="do_subscribed" name="do" type="radio" value="subscribed" />
                <h4>Watching</h4>
                <span class="description">You receive notifications for all conversations in this repository.</span>
                <span class="js-select-button-text hidden-select-button-text">
                  <span class="octicon octicon-eye-unwatch"></span>
                  Unwatch
                </span>
              </div>
            </div> <!-- /.select-menu-item -->

            <div class="select-menu-item js-navigation-item " role="menuitem" tabindex="0">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <div class="select-menu-item-text">
                <input id="do_ignore" name="do" type="radio" value="ignore" />
                <h4>Ignoring</h4>
                <span class="description">You do not receive any notifications for conversations in this repository.</span>
                <span class="js-select-button-text hidden-select-button-text">
                  <span class="octicon octicon-mute"></span>
                  Stop ignoring
                </span>
              </div>
            </div> <!-- /.select-menu-item -->

          </div> <!-- /.select-menu-list -->

        </div> <!-- /.select-menu-modal -->
      </div> <!-- /.select-menu-modal-holder -->
    </div> <!-- /.select-menu -->

</form>
    </li>

  <li>
  

  <div class="js-toggler-container js-social-container starring-container on">
    <a href="/dimitdim/GetARoom/unstar"
      class="minibutton with-count js-toggler-target star-button starred"
      aria-label="Unstar this repository" title="Unstar dimitdim/GetARoom" data-remote="true" data-method="post" rel="nofollow">
      <span class="octicon octicon-star-delete"></span><span class="text">Unstar</span>
    </a>

    <a href="/dimitdim/GetARoom/star"
      class="minibutton with-count js-toggler-target star-button unstarred"
      aria-label="Star this repository" title="Star dimitdim/GetARoom" data-remote="true" data-method="post" rel="nofollow">
      <span class="octicon octicon-star"></span><span class="text">Star</span>
    </a>

      <a class="social-count js-social-count" href="/dimitdim/GetARoom/stargazers">
        1
      </a>
  </div>

  </li>


        <li>
          <a href="/dimitdim/GetARoom/fork" class="minibutton with-count js-toggler-target fork-button lighter tooltipped-n" title="Fork your own copy of dimitdim/GetARoom to your account" aria-label="Fork your own copy of dimitdim/GetARoom to your account" rel="nofollow" data-method="post">
            <span class="octicon octicon-git-branch-create"></span><span class="text">Fork</span>
          </a>
          <a href="/dimitdim/GetARoom/network" class="social-count">1</a>
        </li>


</ul>

        <h1 itemscope itemtype="http://data-vocabulary.org/Breadcrumb" class="entry-title public">
          <span class="repo-label"><span>public</span></span>
          <span class="mega-octicon octicon-repo"></span>
          <span class="author"><a href="/dimitdim" class="url fn" itemprop="url" rel="author"><span itemprop="title">dimitdim</span></a></span><!--
       --><span class="path-divider">/</span><!--
       --><strong><a href="/dimitdim/GetARoom" class="js-current-repository js-repo-home-link">GetARoom</a></strong>

          <span class="page-context-loader">
            <img alt="Octocat-spinner-32" height="16" src="https://github.global.ssl.fastly.net/images/spinners/octocat-spinner-32.gif" width="16" />
          </span>

        </h1>
      </div><!-- /.container -->
    </div><!-- /.repohead -->

    <div class="container">
      <div class="repository-with-sidebar repo-container new-discussion-timeline js-new-discussion-timeline  ">
        <div class="repository-sidebar clearfix">
            

<div class="sunken-menu vertical-right repo-nav js-repo-nav js-repository-container-pjax js-octicon-loaders">
  <div class="sunken-menu-contents">
    <ul class="sunken-menu-group">
      <li class="tooltipped tooltipped-w" aria-label="Code">
        <a href="/dimitdim/GetARoom" aria-label="Code" class="selected js-selected-navigation-item sunken-menu-item" data-hotkey="g c" data-pjax="true" data-selected-links="repo_source repo_downloads repo_commits repo_releases repo_tags repo_branches /dimitdim/GetARoom">
          <span class="octicon octicon-code"></span> <span class="full-word">Code</span>
          <img alt="Octocat-spinner-32" class="mini-loader" height="16" src="https://github.global.ssl.fastly.net/images/spinners/octocat-spinner-32.gif" width="16" />
</a>      </li>

        <li class="tooltipped tooltipped-w" aria-label="Issues">
          <a href="/dimitdim/GetARoom/issues" aria-label="Issues" class="js-selected-navigation-item sunken-menu-item js-disable-pjax" data-hotkey="g i" data-selected-links="repo_issues /dimitdim/GetARoom/issues">
            <span class="octicon octicon-issue-opened"></span> <span class="full-word">Issues</span>
            <span class='counter'>0</span>
            <img alt="Octocat-spinner-32" class="mini-loader" height="16" src="https://github.global.ssl.fastly.net/images/spinners/octocat-spinner-32.gif" width="16" />
</a>        </li>

      <li class="tooltipped tooltipped-w" aria-label="Pull Requests">
        <a href="/dimitdim/GetARoom/pulls" aria-label="Pull Requests" class="js-selected-navigation-item sunken-menu-item js-disable-pjax" data-hotkey="g p" data-selected-links="repo_pulls /dimitdim/GetARoom/pulls">
            <span class="octicon octicon-git-pull-request"></span> <span class="full-word">Pull Requests</span>
            <span class='counter'>0</span>
            <img alt="Octocat-spinner-32" class="mini-loader" height="16" src="https://github.global.ssl.fastly.net/images/spinners/octocat-spinner-32.gif" width="16" />
</a>      </li>


        <li class="tooltipped tooltipped-w" aria-label="Wiki">
          <a href="/dimitdim/GetARoom/wiki" aria-label="Wiki" class="js-selected-navigation-item sunken-menu-item" data-pjax="true" data-selected-links="repo_wiki /dimitdim/GetARoom/wiki">
            <span class="octicon octicon-book"></span> <span class="full-word">Wiki</span>
            <img alt="Octocat-spinner-32" class="mini-loader" height="16" src="https://github.global.ssl.fastly.net/images/spinners/octocat-spinner-32.gif" width="16" />
</a>        </li>
    </ul>
    <div class="sunken-menu-separator"></div>
    <ul class="sunken-menu-group">

      <li class="tooltipped tooltipped-w" aria-label="Pulse">
        <a href="/dimitdim/GetARoom/pulse" aria-label="Pulse" class="js-selected-navigation-item sunken-menu-item" data-pjax="true" data-selected-links="pulse /dimitdim/GetARoom/pulse">
          <span class="octicon octicon-pulse"></span> <span class="full-word">Pulse</span>
          <img alt="Octocat-spinner-32" class="mini-loader" height="16" src="https://github.global.ssl.fastly.net/images/spinners/octocat-spinner-32.gif" width="16" />
</a>      </li>

      <li class="tooltipped tooltipped-w" aria-label="Graphs">
        <a href="/dimitdim/GetARoom/graphs" aria-label="Graphs" class="js-selected-navigation-item sunken-menu-item" data-pjax="true" data-selected-links="repo_graphs repo_contributors /dimitdim/GetARoom/graphs">
          <span class="octicon octicon-graph"></span> <span class="full-word">Graphs</span>
          <img alt="Octocat-spinner-32" class="mini-loader" height="16" src="https://github.global.ssl.fastly.net/images/spinners/octocat-spinner-32.gif" width="16" />
</a>      </li>

      <li class="tooltipped tooltipped-w" aria-label="Network">
        <a href="/dimitdim/GetARoom/network" aria-label="Network" class="js-selected-navigation-item sunken-menu-item js-disable-pjax" data-selected-links="repo_network /dimitdim/GetARoom/network">
          <span class="octicon octicon-git-branch"></span> <span class="full-word">Network</span>
          <img alt="Octocat-spinner-32" class="mini-loader" height="16" src="https://github.global.ssl.fastly.net/images/spinners/octocat-spinner-32.gif" width="16" />
</a>      </li>
    </ul>


      <div class="sunken-menu-separator"></div>
      <ul class="sunken-menu-group">
        <li class="tooltipped tooltipped-w" aria-label="Settings">
          <a href="/dimitdim/GetARoom/settings" aria-label="Settings" class="js-selected-navigation-item sunken-menu-item" data-pjax="true" data-selected-links="repo_settings /dimitdim/GetARoom/settings">
            <span class="octicon octicon-tools"></span> <span class="full-word">Settings</span>
            <img alt="Octocat-spinner-32" class="mini-loader" height="16" src="https://github.global.ssl.fastly.net/images/spinners/octocat-spinner-32.gif" width="16" />
</a>        </li>
      </ul>
  </div>
</div>

              <div class="only-with-full-nav">
                

  

<div class="clone-url open"
  data-protocol-type="http"
  data-url="/users/set_protocol?protocol_selector=http&amp;protocol_type=push">
  <h3><strong>HTTPS</strong> clone URL</h3>
  <div class="clone-url-box">
    <input type="text" class="clone js-url-field"
           value="https://github.com/dimitdim/GetARoom.git" readonly="readonly">

    <span aria-label="copy to clipboard" class="js-zeroclipboard url-box-clippy minibutton zeroclipboard-button" data-clipboard-text="https://github.com/dimitdim/GetARoom.git" data-copied-hint="copied!"><span class="octicon octicon-clippy"></span></span>
  </div>
</div>

  

<div class="clone-url "
  data-protocol-type="ssh"
  data-url="/users/set_protocol?protocol_selector=ssh&amp;protocol_type=push">
  <h3><strong>SSH</strong> clone URL</h3>
  <div class="clone-url-box">
    <input type="text" class="clone js-url-field"
           value="git@github.com:dimitdim/GetARoom.git" readonly="readonly">

    <span aria-label="copy to clipboard" class="js-zeroclipboard url-box-clippy minibutton zeroclipboard-button" data-clipboard-text="git@github.com:dimitdim/GetARoom.git" data-copied-hint="copied!"><span class="octicon octicon-clippy"></span></span>
  </div>
</div>

  

<div class="clone-url "
  data-protocol-type="subversion"
  data-url="/users/set_protocol?protocol_selector=subversion&amp;protocol_type=push">
  <h3><strong>Subversion</strong> checkout URL</h3>
  <div class="clone-url-box">
    <input type="text" class="clone js-url-field"
           value="https://github.com/dimitdim/GetARoom" readonly="readonly">

    <span aria-label="copy to clipboard" class="js-zeroclipboard url-box-clippy minibutton zeroclipboard-button" data-clipboard-text="https://github.com/dimitdim/GetARoom" data-copied-hint="copied!"><span class="octicon octicon-clippy"></span></span>
  </div>
</div>


<p class="clone-options">You can clone with
      <a href="#" class="js-clone-selector" data-protocol="http">HTTPS</a>,
      <a href="#" class="js-clone-selector" data-protocol="ssh">SSH</a>,
      or <a href="#" class="js-clone-selector" data-protocol="subversion">Subversion</a>.
  <span class="help tooltipped tooltipped-n" aria-label="Get help on which URL is right for you.">
    <a href="https://help.github.com/articles/which-remote-url-should-i-use">
    <span class="octicon octicon-question"></span>
    </a>
  </span>
</p>


  <a href="github-windows://openRepo/https://github.com/dimitdim/GetARoom" class="minibutton sidebar-button" title="Save dimitdim/GetARoom to your computer and use it in GitHub Desktop." aria-label="Save dimitdim/GetARoom to your computer and use it in GitHub Desktop.">
    <span class="octicon octicon-device-desktop"></span>
    Clone in Desktop
  </a>

                <a href="/dimitdim/GetARoom/archive/master.zip"
                   class="minibutton sidebar-button"
                   aria-label="Download dimitdim/GetARoom as a zip file"
                   title="Download dimitdim/GetARoom as a zip file"
                   rel="nofollow">
                  <span class="octicon octicon-cloud-download"></span>
                  Download ZIP
                </a>
              </div>
        </div><!-- /.repository-sidebar -->

        <div id="js-repo-pjax-container" class="repository-content context-loader-container" data-pjax-container>
          

<a href="/dimitdim/GetARoom/blame/8641978a94567c8f386bd9a997b0b146c668abfe/Main/app/views.py" class="hidden" data-hotkey="y">Permalink</a>

<!-- blob contrib key: blob_contributors:v21:e09ee61d10ded5271f3e3f58af639e7e -->

<p title="This is a placeholder element" class="js-history-link-replace hidden"></p>

<a href="/dimitdim/GetARoom/find/master" data-pjax data-hotkey="t" class="js-show-file-finder" style="display:none">Show File Finder</a>

<div class="file-navigation">
  

<div class="select-menu js-menu-container js-select-menu" >
  <span class="minibutton select-menu-button js-menu-target" data-hotkey="w"
    data-master-branch="master"
    data-ref="master"
    role="button" aria-label="Switch branches or tags" tabindex="0" aria-haspopup="true">
    <span class="octicon octicon-git-branch"></span>
    <i>branch:</i>
    <span class="js-select-button">master</span>
  </span>

  <div class="select-menu-modal-holder js-menu-content js-navigation-container" data-pjax aria-hidden="true">

    <div class="select-menu-modal">
      <div class="select-menu-header">
        <span class="select-menu-title">Switch branches/tags</span>
        <span class="octicon octicon-remove-close js-menu-close"></span>
      </div> <!-- /.select-menu-header -->

      <div class="select-menu-filters">
        <div class="select-menu-text-filter">
          <input type="text" aria-label="Find or create a branch…" id="context-commitish-filter-field" class="js-filterable-field js-navigation-enable" placeholder="Find or create a branch…">
        </div>
        <div class="select-menu-tabs">
          <ul>
            <li class="select-menu-tab">
              <a href="#" data-tab-filter="branches" class="js-select-menu-tab">Branches</a>
            </li>
            <li class="select-menu-tab">
              <a href="#" data-tab-filter="tags" class="js-select-menu-tab">Tags</a>
            </li>
          </ul>
        </div><!-- /.select-menu-tabs -->
      </div><!-- /.select-menu-filters -->

      <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket" data-tab-filter="branches">

        <div data-filterable-for="context-commitish-filter-field" data-filterable-type="substring">


            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/dimitdim/GetARoom/blob/gh-pages/Main/app/views.py"
                 data-name="gh-pages"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="gh-pages">gh-pages</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item selected">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/dimitdim/GetARoom/blob/master/Main/app/views.py"
                 data-name="master"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="master">master</a>
            </div> <!-- /.select-menu-item -->
        </div>

          <form accept-charset="UTF-8" action="/dimitdim/GetARoom/branches" class="js-create-branch select-menu-item select-menu-new-item-form js-navigation-item js-new-item-form" method="post"><div style="margin:0;padding:0;display:inline"><input name="authenticity_token" type="hidden" value="I4ksMpnqk9u1Ro7NpebDXTlJVQf95feMVyxLs0SIUZFgy0gp8VO2/5rICy1cymbVWWa/KaboBR3a4Q7mVTsTUg==" /></div>
            <span class="octicon octicon-git-branch-create select-menu-item-icon"></span>
            <div class="select-menu-item-text">
              <h4>Create branch: <span class="js-new-item-name"></span></h4>
              <span class="description">from ‘master’</span>
            </div>
            <input type="hidden" name="name" id="name" class="js-new-item-value">
            <input type="hidden" name="branch" id="branch" value="master" />
            <input type="hidden" name="path" id="path" value="Main/app/views.py" />
          </form> <!-- /.select-menu-item -->

      </div> <!-- /.select-menu-list -->

      <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket" data-tab-filter="tags">
        <div data-filterable-for="context-commitish-filter-field" data-filterable-type="substring">


        </div>

        <div class="select-menu-no-results">Nothing to show</div>
      </div> <!-- /.select-menu-list -->

    </div> <!-- /.select-menu-modal -->
  </div> <!-- /.select-menu-modal-holder -->
</div> <!-- /.select-menu -->

  <div class="breadcrumb">
    <span class='repo-root js-repo-root'><span itemscope="" itemtype="http://data-vocabulary.org/Breadcrumb"><a href="/dimitdim/GetARoom" data-branch="master" data-direction="back" data-pjax="true" itemscope="url"><span itemprop="title">GetARoom</span></a></span></span><span class="separator"> / </span><span itemscope="" itemtype="http://data-vocabulary.org/Breadcrumb"><a href="/dimitdim/GetARoom/tree/master/Main" data-branch="master" data-direction="back" data-pjax="true" itemscope="url"><span itemprop="title">Main</span></a></span><span class="separator"> / </span><span itemscope="" itemtype="http://data-vocabulary.org/Breadcrumb"><a href="/dimitdim/GetARoom/tree/master/Main/app" data-branch="master" data-direction="back" data-pjax="true" itemscope="url"><span itemprop="title">app</span></a></span><span class="separator"> / </span><strong class="final-path">views.py</strong> <span aria-label="copy to clipboard" class="js-zeroclipboard minibutton zeroclipboard-button" data-clipboard-text="Main/app/views.py" data-copied-hint="copied!"><span class="octicon octicon-clippy"></span></span>
  </div>
</div>


  <div class="commit commit-loader file-history-tease js-deferred-content" data-url="/dimitdim/GetARoom/contributors/master/Main/app/views.py">
    Fetching contributors…

    <div class="participation">
      <p class="loader-loading"><img alt="Octocat-spinner-32-eaf2f5" height="16" src="https://github.global.ssl.fastly.net/images/spinners/octocat-spinner-32-EAF2F5.gif" width="16" /></p>
      <p class="loader-error">Cannot retrieve contributors at this time</p>
    </div>
  </div>

<div class="file-box">
  <div class="file">
    <div class="meta clearfix">
      <div class="info file-name">
        <span class="icon"><b class="octicon octicon-file-text"></b></span>
        <span class="mode" title="File Mode">file</span>
        <span class="meta-divider"></span>
          <span>65 lines (52 sloc)</span>
          <span class="meta-divider"></span>
        <span>2.08 kb</span>
      </div>
      <div class="actions">
        <div class="button-group">
            <a class="minibutton tooltipped tooltipped-w"
               href="github-windows://openRepo/https://github.com/dimitdim/GetARoom?branch=master&amp;filepath=Main%2Fapp%2Fviews.py" aria-label="Open this file in GitHub for Windows">
                <span class="octicon octicon-device-desktop"></span> Open
            </a>
                <a class="minibutton js-update-url-with-hash"
                   href="/dimitdim/GetARoom/edit/master/Main/app/views.py"
                   data-method="post" rel="nofollow" data-hotkey="e">Edit</a>
          <a href="/dimitdim/GetARoom/raw/master/Main/app/views.py" class="button minibutton " id="raw-url">Raw</a>
            <a href="/dimitdim/GetARoom/blame/master/Main/app/views.py" class="button minibutton js-update-url-with-hash">Blame</a>
          <a href="/dimitdim/GetARoom/commits/master/Main/app/views.py" class="button minibutton " rel="nofollow">History</a>
        </div><!-- /.button-group -->

            <a class="minibutton danger empty-icon"
               href="/dimitdim/GetARoom/delete/master/Main/app/views.py"
               data-method="post" data-test-id="delete-blob-file" rel="nofollow">

          Delete
        </a>
      </div><!-- /.actions -->
    </div>
        <div class="blob-wrapper data type-python js-blob-data">
        <table class="file-code file-diff tab-size-8">
          <tr class="file-code-line">
            <td class="blob-line-nums">
              <span id="L1" rel="#L1">1</span>
<span id="L2" rel="#L2">2</span>
<span id="L3" rel="#L3">3</span>
<span id="L4" rel="#L4">4</span>
<span id="L5" rel="#L5">5</span>
<span id="L6" rel="#L6">6</span>
<span id="L7" rel="#L7">7</span>
<span id="L8" rel="#L8">8</span>
<span id="L9" rel="#L9">9</span>
<span id="L10" rel="#L10">10</span>
<span id="L11" rel="#L11">11</span>
<span id="L12" rel="#L12">12</span>
<span id="L13" rel="#L13">13</span>
<span id="L14" rel="#L14">14</span>
<span id="L15" rel="#L15">15</span>
<span id="L16" rel="#L16">16</span>
<span id="L17" rel="#L17">17</span>
<span id="L18" rel="#L18">18</span>
<span id="L19" rel="#L19">19</span>
<span id="L20" rel="#L20">20</span>
<span id="L21" rel="#L21">21</span>
<span id="L22" rel="#L22">22</span>
<span id="L23" rel="#L23">23</span>
<span id="L24" rel="#L24">24</span>
<span id="L25" rel="#L25">25</span>
<span id="L26" rel="#L26">26</span>
<span id="L27" rel="#L27">27</span>
<span id="L28" rel="#L28">28</span>
<span id="L29" rel="#L29">29</span>
<span id="L30" rel="#L30">30</span>
<span id="L31" rel="#L31">31</span>
<span id="L32" rel="#L32">32</span>
<span id="L33" rel="#L33">33</span>
<span id="L34" rel="#L34">34</span>
<span id="L35" rel="#L35">35</span>
<span id="L36" rel="#L36">36</span>
<span id="L37" rel="#L37">37</span>
<span id="L38" rel="#L38">38</span>
<span id="L39" rel="#L39">39</span>
<span id="L40" rel="#L40">40</span>
<span id="L41" rel="#L41">41</span>
<span id="L42" rel="#L42">42</span>
<span id="L43" rel="#L43">43</span>
<span id="L44" rel="#L44">44</span>
<span id="L45" rel="#L45">45</span>
<span id="L46" rel="#L46">46</span>
<span id="L47" rel="#L47">47</span>
<span id="L48" rel="#L48">48</span>
<span id="L49" rel="#L49">49</span>
<span id="L50" rel="#L50">50</span>
<span id="L51" rel="#L51">51</span>
<span id="L52" rel="#L52">52</span>
<span id="L53" rel="#L53">53</span>
<span id="L54" rel="#L54">54</span>
<span id="L55" rel="#L55">55</span>
<span id="L56" rel="#L56">56</span>
<span id="L57" rel="#L57">57</span>
<span id="L58" rel="#L58">58</span>
<span id="L59" rel="#L59">59</span>
<span id="L60" rel="#L60">60</span>
<span id="L61" rel="#L61">61</span>
<span id="L62" rel="#L62">62</span>
<span id="L63" rel="#L63">63</span>
<span id="L64" rel="#L64">64</span>

            </td>
            <td class="blob-line-code"><div class="code-body highlight"><pre><div class='line' id='LC1'><span class="kn">from</span> <span class="nn">app</span> <span class="kn">import</span> <span class="n">app</span><span class="p">,</span> <span class="n">db</span><span class="p">,</span> <span class="n">lm</span><span class="p">,</span> <span class="n">oid</span></div><div class='line' id='LC2'><span class="kn">from</span> <span class="nn">flask</span> <span class="kn">import</span> <span class="n">render_template</span><span class="p">,</span> <span class="n">flash</span><span class="p">,</span> <span class="n">redirect</span><span class="p">,</span> <span class="n">session</span><span class="p">,</span> <span class="n">url_for</span><span class="p">,</span> <span class="n">request</span><span class="p">,</span> <span class="n">g</span></div><div class='line' id='LC3'><span class="kn">import</span> <span class="nn">time</span></div><div class='line' id='LC4'><span class="kn">from</span> <span class="nn">flask.ext.login</span> <span class="kn">import</span> <span class="n">login_user</span><span class="p">,</span> <span class="n">logout_user</span><span class="p">,</span> <span class="n">current_user</span><span class="p">,</span> <span class="n">login_required</span></div><div class='line' id='LC5'><span class="kn">from</span> <span class="nn">forms</span> <span class="kn">import</span> <span class="n">LoginForm</span></div><div class='line' id='LC6'><span class="kn">from</span> <span class="nn">models</span> <span class="kn">import</span> <span class="n">User</span><span class="p">,</span> <span class="n">ROLE_USER</span><span class="p">,</span> <span class="n">ROLE_ADMIN</span></div><div class='line' id='LC7'><br/></div><div class='line' id='LC8'><br/></div><div class='line' id='LC9'><span class="n">user</span> <span class="o">=</span> <span class="p">{</span><span class="s">&#39;nick&#39;</span><span class="p">:</span> <span class="s">&#39;dimitdim&#39;</span><span class="p">,</span> <span class="s">&#39;name&#39;</span><span class="p">:</span> <span class="s">&#39;Dimitar&#39;</span><span class="p">}</span></div><div class='line' id='LC10'><span class="n">tim</span> <span class="o">=</span> <span class="nb">str</span><span class="p">(</span><span class="n">time</span><span class="o">.</span><span class="n">asctime</span><span class="p">(</span><span class="n">time</span><span class="o">.</span><span class="n">localtime</span><span class="p">()))</span></div><div class='line' id='LC11'><br/></div><div class='line' id='LC12'><br/></div><div class='line' id='LC13'><span class="nd">@app.route</span><span class="p">(</span><span class="s">&#39;/&#39;</span><span class="p">)</span></div><div class='line' id='LC14'><span class="nd">@app.route</span><span class="p">(</span><span class="s">&#39;/index&#39;</span><span class="p">)</span></div><div class='line' id='LC15'><span class="k">def</span> <span class="nf">index</span><span class="p">():</span></div><div class='line' id='LC16'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">title</span> <span class="o">=</span> <span class="s">&#39;test&#39;</span></div><div class='line' id='LC17'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">render_template</span><span class="p">(</span><span class="s">&quot;index.html&quot;</span><span class="p">,</span> <span class="n">title</span><span class="o">=</span><span class="n">title</span><span class="p">,</span> <span class="n">user</span><span class="o">=</span><span class="n">user</span><span class="p">,</span> <span class="n">time</span><span class="o">=</span><span class="n">tim</span><span class="p">)</span></div><div class='line' id='LC18'><br/></div><div class='line' id='LC19'><br/></div><div class='line' id='LC20'><span class="nd">@app.route</span><span class="p">(</span><span class="s">&#39;/login&#39;</span><span class="p">,</span> <span class="n">methods</span><span class="o">=</span><span class="p">[</span><span class="s">&#39;GET&#39;</span><span class="p">,</span> <span class="s">&#39;POST&#39;</span><span class="p">])</span></div><div class='line' id='LC21'><span class="nd">@oid.loginhandler</span></div><div class='line' id='LC22'><span class="k">def</span> <span class="nf">login</span><span class="p">():</span></div><div class='line' id='LC23'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">form</span> <span class="o">=</span> <span class="n">LoginForm</span><span class="p">()</span></div><div class='line' id='LC24'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">title</span> <span class="o">=</span> <span class="s">&#39;Sign In&#39;</span></div><div class='line' id='LC25'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">providers</span> <span class="o">=</span> <span class="n">app</span><span class="o">.</span><span class="n">config</span><span class="p">[</span><span class="s">&#39;OPENID_PROVIDERS&#39;</span><span class="p">]</span></div><div class='line' id='LC26'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">g</span><span class="o">.</span><span class="n">user</span> <span class="ow">is</span> <span class="ow">not</span> <span class="bp">None</span> <span class="ow">and</span> <span class="n">g</span><span class="o">.</span><span class="n">user</span><span class="o">.</span><span class="n">is_authenticated</span><span class="p">():</span></div><div class='line' id='LC27'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">redirect</span><span class="p">(</span><span class="n">url_for</span><span class="p">(</span><span class="s">&#39;index&#39;</span><span class="p">))</span></div><div class='line' id='LC28'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">form</span><span class="o">.</span><span class="n">validate_on_submit</span><span class="p">():</span></div><div class='line' id='LC29'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">flash</span><span class="p">(</span><span class="s">&#39;OpenID: &#39;</span> <span class="o">+</span> <span class="n">form</span><span class="o">.</span><span class="n">openid</span><span class="o">.</span><span class="n">data</span><span class="p">)</span></div><div class='line' id='LC30'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">flash</span><span class="p">(</span><span class="s">&#39;Cookie: &#39;</span> <span class="o">+</span> <span class="nb">str</span><span class="p">(</span><span class="n">form</span><span class="o">.</span><span class="n">remember_me</span><span class="o">.</span><span class="n">data</span><span class="p">))</span></div><div class='line' id='LC31'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">session</span><span class="p">[</span><span class="s">&#39;remember_me&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="n">form</span><span class="o">.</span><span class="n">remember_me</span><span class="o">.</span><span class="n">data</span></div><div class='line' id='LC32'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">oid</span><span class="o">.</span><span class="n">try_login</span><span class="p">(</span><span class="n">form</span><span class="o">.</span><span class="n">openid</span><span class="o">.</span><span class="n">data</span><span class="p">,</span> <span class="n">ask_for</span><span class="o">=</span><span class="p">[</span><span class="s">&#39;nickname&#39;</span><span class="p">,</span> <span class="s">&#39;email&#39;</span><span class="p">])</span></div><div class='line' id='LC33'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">render_template</span><span class="p">(</span><span class="s">&quot;login.html&quot;</span><span class="p">,</span> <span class="n">title</span><span class="o">=</span><span class="n">title</span><span class="p">,</span> <span class="n">form</span><span class="o">=</span><span class="n">form</span><span class="p">,</span> <span class="n">user</span><span class="o">=</span><span class="n">user</span><span class="p">,</span> <span class="n">time</span><span class="o">=</span><span class="n">tim</span><span class="p">,</span> <span class="n">providers</span><span class="o">=</span><span class="n">providers</span><span class="p">)</span></div><div class='line' id='LC34'><br/></div><div class='line' id='LC35'><br/></div><div class='line' id='LC36'><span class="nd">@app.route</span><span class="p">(</span><span class="s">&#39;/css&#39;</span><span class="p">)</span></div><div class='line' id='LC37'><span class="k">def</span> <span class="nf">css</span><span class="p">():</span></div><div class='line' id='LC38'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">render_template</span><span class="p">(</span><span class="s">&quot;default.css&quot;</span><span class="p">)</span></div><div class='line' id='LC39'><br/></div><div class='line' id='LC40'><br/></div><div class='line' id='LC41'><span class="nd">@lm.user_loader</span></div><div class='line' id='LC42'><span class="k">def</span> <span class="nf">load_user</span><span class="p">(</span><span class="nb">id</span><span class="p">):</span></div><div class='line' id='LC43'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">User</span><span class="o">.</span><span class="n">query</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="nb">int</span><span class="p">(</span><span class="nb">id</span><span class="p">))</span></div><div class='line' id='LC44'><br/></div><div class='line' id='LC45'><br/></div><div class='line' id='LC46'><span class="nd">@oid.after_login</span></div><div class='line' id='LC47'><span class="k">def</span> <span class="nf">after_login</span><span class="p">(</span><span class="n">resp</span><span class="p">):</span></div><div class='line' id='LC48'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">resp</span><span class="o">.</span><span class="n">email</span> <span class="ow">is</span> <span class="bp">None</span> <span class="ow">or</span> <span class="n">resp</span><span class="o">.</span><span class="n">email</span> <span class="o">==</span> <span class="s">&quot;&quot;</span><span class="p">:</span></div><div class='line' id='LC49'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">flash</span><span class="p">(</span><span class="s">&#39;Invalid login. Please try again.&#39;</span><span class="p">)</span></div><div class='line' id='LC50'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">redirect</span><span class="p">(</span><span class="n">url_for</span><span class="p">(</span><span class="s">&#39;login&#39;</span><span class="p">))</span></div><div class='line' id='LC51'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">user</span> <span class="o">=</span> <span class="n">User</span><span class="o">.</span><span class="n">query</span><span class="o">.</span><span class="n">filter_by</span><span class="p">(</span><span class="n">email</span><span class="o">=</span><span class="n">resp</span><span class="o">.</span><span class="n">email</span><span class="p">)</span><span class="o">.</span><span class="n">first</span><span class="p">()</span></div><div class='line' id='LC52'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">user</span> <span class="ow">is</span> <span class="bp">None</span><span class="p">:</span></div><div class='line' id='LC53'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">nickname</span> <span class="o">=</span> <span class="n">resp</span><span class="o">.</span><span class="n">nickname</span></div><div class='line' id='LC54'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">nickname</span> <span class="ow">is</span> <span class="bp">None</span> <span class="ow">or</span> <span class="n">nickname</span> <span class="o">==</span> <span class="s">&quot;&quot;</span><span class="p">:</span></div><div class='line' id='LC55'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">nickname</span> <span class="o">=</span> <span class="n">resp</span><span class="o">.</span><span class="n">email</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s">&#39;@&#39;</span><span class="p">)[</span><span class="mi">0</span><span class="p">]</span></div><div class='line' id='LC56'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">user</span> <span class="o">=</span> <span class="n">User</span><span class="p">(</span><span class="n">nickname</span><span class="o">=</span><span class="n">nickname</span><span class="p">,</span> <span class="n">email</span><span class="o">=</span><span class="n">resp</span><span class="o">.</span><span class="n">email</span><span class="p">,</span> <span class="n">role</span><span class="o">=</span><span class="n">ROLE_USER</span><span class="p">)</span></div><div class='line' id='LC57'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">db</span><span class="o">.</span><span class="n">session</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">user</span><span class="p">)</span></div><div class='line' id='LC58'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">db</span><span class="o">.</span><span class="n">session</span><span class="o">.</span><span class="n">commit</span><span class="p">()</span></div><div class='line' id='LC59'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">remember_me</span> <span class="o">=</span> <span class="bp">False</span></div><div class='line' id='LC60'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="s">&#39;remember_me&#39;</span> <span class="ow">in</span> <span class="n">session</span><span class="p">:</span></div><div class='line' id='LC61'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">remember_me</span> <span class="o">=</span> <span class="n">session</span><span class="p">[</span><span class="s">&#39;remember_me&#39;</span><span class="p">]</span></div><div class='line' id='LC62'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">session</span><span class="o">.</span><span class="n">pop</span><span class="p">(</span><span class="s">&#39;remember_me&#39;</span><span class="p">,</span> <span class="bp">None</span><span class="p">)</span></div><div class='line' id='LC63'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">login_user</span><span class="p">(</span><span class="n">user</span><span class="p">,</span> <span class="n">remember</span><span class="o">=</span><span class="n">remember_me</span><span class="p">)</span></div><div class='line' id='LC64'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">redirect</span><span class="p">(</span><span class="n">request</span><span class="o">.</span><span class="n">args</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s">&#39;next&#39;</span><span class="p">)</span> <span class="ow">or</span> <span class="n">url_for</span><span class="p">(</span><span class="s">&#39;index&#39;</span><span class="p">))</span></div></pre></div></td>
          </tr>
        </table>
  </div>

  </div>
</div>

<a href="#jump-to-line" rel="facebox[.linejump]" data-hotkey="l" class="js-jump-to-line" style="display:none">Jump to Line</a>
<div id="jump-to-line" style="display:none">
  <form accept-charset="UTF-8" class="js-jump-to-line-form">
    <input class="linejump-input js-jump-to-line-field" type="text" placeholder="Jump to line&hellip;" autofocus>
    <button type="submit" class="button">Go</button>
  </form>
</div>

        </div>

      </div><!-- /.repo-container -->
      <div class="modal-backdrop"></div>
    </div><!-- /.container -->
  </div><!-- /.site -->


    </div><!-- /.wrapper -->

      <div class="container">
  <div class="site-footer">
    <ul class="site-footer-links right">
      <li><a href="https://status.github.com/">Status</a></li>
      <li><a href="http://developer.github.com">API</a></li>
      <li><a href="http://training.github.com">Training</a></li>
      <li><a href="http://shop.github.com">Shop</a></li>
      <li><a href="/blog">Blog</a></li>
      <li><a href="/about">About</a></li>

    </ul>

    <a href="/">
      <span class="mega-octicon octicon-mark-github" title="GitHub"></span>
    </a>

    <ul class="site-footer-links">
      <li>&copy; 2014 <span title="0.05747s from github-fe127-cp1-prd.iad.github.net">GitHub</span>, Inc.</li>
        <li><a href="/site/terms">Terms</a></li>
        <li><a href="/site/privacy">Privacy</a></li>
        <li><a href="/security">Security</a></li>
        <li><a href="/contact">Contact</a></li>
    </ul>
  </div><!-- /.site-footer -->
</div><!-- /.container -->


    <div class="fullscreen-overlay js-fullscreen-overlay" id="fullscreen_overlay">
  <div class="fullscreen-container js-fullscreen-container">
    <div class="textarea-wrap">
      <textarea name="fullscreen-contents" id="fullscreen-contents" class="fullscreen-contents js-fullscreen-contents" placeholder="" data-suggester="fullscreen_suggester"></textarea>
    </div>
  </div>
  <div class="fullscreen-sidebar">
    <a href="#" class="exit-fullscreen js-exit-fullscreen tooltipped tooltipped-w" aria-label="Exit Zen Mode">
      <span class="mega-octicon octicon-screen-normal"></span>
    </a>
    <a href="#" class="theme-switcher js-theme-switcher tooltipped tooltipped-w"
      aria-label="Switch themes">
      <span class="octicon octicon-color-mode"></span>
    </a>
  </div>
</div>



    <div id="ajax-error-message" class="flash flash-error">
      <span class="octicon octicon-alert"></span>
      <a href="#" class="octicon octicon-remove-close close js-ajax-error-dismiss"></a>
      Something went wrong with that request. Please try again.
    </div>

  </body>
</html>

