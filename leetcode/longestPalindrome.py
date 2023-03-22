def isPalindrome(s):
    return s == s[::-1]


def longestPalindrome(s):
    if len(s) == 1:
        return s

    longest = ''
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            temp = s[i:j + 1]
            if isPalindrome(temp):
                if len(temp) > len(longest):
                    longest = temp

    if longest == '':
        longest = s[0]

    return longest



string = "yfikrcvmuegdciuqahlsjesplljlswxaejgdzhubzqkiroxyhtjvazcwcnsvdzjiainmiyobyfclyugttaswlntwukkfbebcdaxdpaxwqenkxxphxdcgrnpruoaetvunwyskswvvmjmltncsdukwzlpfodhgxkjvzppwpvmqlfbojgbdiryleskemhjfoxxzjqihcykpgzhaugwwbqtddjzpmrgdncgzsttqenmbnnavfjkiennwxtguywoaiuungqpyfcffzmljfianapawiayywuvazrnxouvndzqbmmyntkkdyykgodjbeojtpnsyhfrltuazgznddaaibupephvgrcjpzvjttmhtnydwvrpgijselaukwrcosxpcbptebalkheymuyblffahvbszotmutmmqhlgoskuoejvavlprvgyozpylsnqhqrnqpabgbwzwxyibpmsauxcfnbtwwbosksuzqzmobijytxxtyjibomzqzusksobwwtbnfcxuasmpbiyxwzwbgbapqnrqhqnslypzoygvrplvavjeouksoglhqmmtumtozsbvhafflbyumyehklabetpbcpxsocrwkualesjigprvwdynthmttjvzpjcrgvhpepubiaaddnzgzautlrfhysnptjoebjdogkyydkktnymmbqzdnvuoxnrzavuwyyaiwapanaifjlmzffcfypqgnuuiaowyugtxwnneikjfvannbmneqttszgcndgrmpzjddtqbwwguahzgpkychiqjzxxofjhmekselyridbgjobflqmvpwppzvjkxghdofplzwkudscntlmjmvvwsksywnuvteaourpnrgcdxhpxxkneqwxapdxadcbebfkkuwtnlwsattguylcfyboyimniaijzdvsncwczavjthyxorikqzbuhzdgjeaxwsljllpsejslhaquicdgeumvcrkify"

print(longestPalindrome(string))