∇ ReadAndProcessFile
    ⍝ Open the file and read its content
    fileName ← 'flag.txt.enc'
    encContent ← ⎕CR 'cat ', fileName  ⍝ Reads file content as text

    ⍝ Display confirmation
    'Content written to flag.txt:', encContent ⎕← ''
∇
