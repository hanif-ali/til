# Vertically Aligning Images with Text in Github Markdown

Sometimes when you have images in the middle of the text, you want have control on how it is aligned. For instance, you may want to center it with respect to the paragraph, so that no matter what size the image is, the paragraph touches its center. In HTML, this can be acheived through the `vertical-align` CSS property, but this doesn't work in Github Markdown. Instead, use the `valign` attribute. e.g.,

```
<p>This text has an icon embedded <img src="/source/to/image" valign="middle"></p
```

This will center the image with respect to the text.
