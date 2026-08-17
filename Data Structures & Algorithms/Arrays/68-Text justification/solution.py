class Solution(object):
    def fullJustify(self, words, maxWidth):
        result = []
        i = 0

        while i < len(words):

            # Find how many words fit in this line
            j = i
            line_length = 0

            while j < len(words):
                word_length = len(words[j])

                # Space is needed before every word except first
                if line_length + word_length + (j - i) > maxWidth:
                    break

                line_length += word_length
                j += 1

            # Words for this line
            line = words[i:j]

            # Last line OR only one word
            if j == len(words) or len(line) == 1:
                text = " ".join(line)
                text += " " * (maxWidth - len(text))

            else:
                # Total spaces that must be distributed
                spaces = maxWidth - sum(len(word) for word in line)

                gaps = len(line) - 1

                # Minimum spaces per gap
                space_each = spaces // gaps

                # Extra spaces
                extra = spaces % gaps

                text = ""

                for k in range(gaps):
                    text += line[k]
                    text += " " * (space_each + (1 if k < extra else 0))

                text += line[-1]

            result.append(text)

            # Move to next line
            i = j

        return result
