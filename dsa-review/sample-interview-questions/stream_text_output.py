"""
You are building a small utility for processing streamed text output. The text arrives in chunks, where each chunk is a string. A special substring called a stop token indicates where the meaningful output ends.

You are given:

chunks: List[str] — streamed pieces of text, in order

stop_token: str — a substring that marks the end of the content

Part 1 — Stop token appears within a chunk

Write a function that concatenates the chunks in order and returns only the text that appears before the first occurrence of stop_token.

If the stop token does not appear anywhere, return the full concatenated text.


"""
def truncate_at_stop_token(chunks: list[str], stop_token: str) -> list[str]:
    output = []
    for chunk in chunks:
        if stop_token in chunk:
            cleaned_str = chunk.split(stop_token)[0]
            output.append(cleaned_str)
            return output
        else:
            output.append(chunk)
    return output


chunks = [
  "Hello there how are you </ENDHERE>",
  "I would like to ask you about",
  "more about yourself"
]
stop_token = "</ENDHERE>"

output = "Hello there how are you "

# print(truncate_at_stop_token(chunks, stop_token))


"""
Part 2 — Stop token may be split across chunks

Now assume the stop token can be split across chunk boundaries. Your function must still return the text before the stop token, even if the stop token is formed by combining characters from multiple consecutive chunks.

If the stop token does not appear anywhere (even across boundaries), return the full concatenated text.

rolling window type question
"""

def truncate_at_stop_token_2(chunks: list[str], stop_token: str) -> list[str]:
    len_token = len(stop_token)
    carry = ""
    out = []

    for chunk in chunks:
        combined = carry + chunk
        pos = combined.find(stop_token)
        if pos != -1:
            out.append(combined[:pos])
            return out
        if len_token > 1:
            safe_len = max(0, len(combined) - (safe_len-1))
            out.append(combined[:safe_len])
            carry = combined[safe_len:]
        else:
            out.append(combined)
            carry = ""

    out.append(carry)
    return out

chunks = [
  "Hello there </END",
  "HERE>I would like to ask you about",
  "more about yourself"
]
stop_token = "</ENDHERE>"

output = "Hello there how are you "

print(truncate_at_stop_token_2(chunks, stop_token))

"""
web request teacher student matching design the endpoint

"""