<!--
The canonical output file. The translation loop appends approved chapters here.

split_book.py expects this structure:
  # Title              → frontmatter (kept whole)
  ## Foreword          → its own page
  ## Part I: ...       → its own page (frontispiece for the part)
  ### Chapter 1: ...   → its own page
  ### Epilogue: ...    → its own page
  ## About the Author  → its own page

Edit split_book.py if your book has different structural elements.
-->
