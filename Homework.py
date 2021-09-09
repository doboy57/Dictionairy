def main():
  infile = open('info_security.txt','r')
  pre_e = infile.read()
  outfile = open('encrypted_text','w')
  text_list = []
  encrypt_key = {'a':'q', 'b':'w', 'd':'e', 'e':'r', 'g':'t', 'c':'y','f':'u','h':'i','i':'o','j':'p','k':'a','l':'s','m':'d','n':'f','o':'g','p':'h','q':'j','r':'k','s':'l','t':'z','u':'21','x':'c','v':'b','w':'v','x':'n','y':'m','z':'23','A':'1',
  'B':'2','C':'3','D':'4','E':'5','F':'6','G':'7','H':'8','I':'9','J':'Q','K':'W','L':'E','M':'R','N':'T','O':'Y','P':'U','Q':'I','R':'O','S':'P','T':'A','U':'S','V':'D','W':'F','X':'G','Y':'H','Z':'J', ' ':'0', '.':'84', ':':'85'  }
  for l in pre_e:
      
      outfile.write(encrypt_key[l])
      



  
main()