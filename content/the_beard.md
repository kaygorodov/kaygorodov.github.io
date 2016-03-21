Title: The Beard - Logicless Template Engine in Scala!
Date: 2016-03-21 15:00
Category: Blog
Tags: The Beard, Scala, template-engine
Author: Andrey Kaygorodov 
Summary: Short introduction into the Beard template engine.

Recently, I was interested in the language design and was reading a few books devoted to it. So, when the opportunity to work on the template engine showed up, I decided not to lose it.
It is called the [Beard](https://github.com/zalando/beard). It is a minimalistic template engine written in Scala. 

How it looks like:

```
<html>
  <body>
    {{if user.isCool}}
      <div>{{user.name}} is cool</div>
    {{else}}
      <div>{{user.name}} is not cool</div>
    {{/if}}
  </body>
</html>
```

Of course, you can use the Beard not only for HTML generation.

Some cool things are:

* Curly braces tags for everything i.e. for the control flow tags such as `{{ if }}` or `{{ for }}` as well as for variable printing `{{ myvar }}`. Usually templates engines have different tags for above things e.g. Django Template Engine `{% if %}`, `{{ variable }}`.

* It uses [ANTLR](http://www.antlr.org/) to generate a parser. ANTLR is a very interesting project itself, and it is very fast.

* There is all the common suff for template engines as blocks, template inheritance, the yeild statement, filters and so on.

* The project follows the good practices as a scala project. There are unit tests, performance tests and sbt used as a build tool.


Even though the project is actually used in a few real projects, there is still room for improvement. I encourage you to participate in the project either you are interested in Scala or grammar/lexer/parser stuff.

I am happy that I had a chance to work on the open source project during my working hours, thanks to my new employer Zalando ([and it is hiring!]http://jobs.zalando.de/en/).
