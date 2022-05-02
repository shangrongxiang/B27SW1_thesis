from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.methods.posts import GetPosts, NewPost
from wordpress_xmlrpc.methods.users import GetUserInfo
from wordpress_xmlrpc.methods import posts
from wordpress_xmlrpc.methods import taxonomies
from wordpress_xmlrpc import WordPressTerm
from wordpress_xmlrpc.compat import xmlrpc_client
from wordpress_xmlrpc.methods import media, posts
from wordpress_xmlrpc import Client, WordPressPost
domain = 'https://b27sw1.wordpress.com//xmlrpc.php'   ##test website
username  ='pecs107'
password ='107srxsrx'

    
def connectWordpress():

    wp = Client(domain,username,password)

def postsimple(title,content,status):

    wp = Client(domain,username,password)

    post = WordPressPost()
    post.title = title
       
    post.content = content    ##  post content

    post.post_status = status   ##post content

   # terms_names1 = terms_names
  #  post.terms_names = terms_names  ##     ##The tag the article belongs to, if not, it will be automatically created

    wp.call(NewPost(post))
        

def tag(taxonomy,tagname,slug):
    taxonomy  = taxonomy
    tagname = tagname
    slug = slug
    wp = Client(domain, name, password)
    
    post = WordPressPost()
        
        
        #creat a tag
    tag = WordPressTerm()
    tag.taxonomy = taxonomy
    tag.name = tagname   #tag name
    tag.slug = slug        #tag slug
    tag.id = wp.call(taxonomies.NewTerm(tag))#tag id

def postwithimag(title,content,status,terms_names):
    wp = Client(domain,username,password)
    filename = './my.jpg' 
    # prepare metadata
    data = {
    'name': 'picture.jpg',
    'type': 'image/jpeg',  # mimetype
    }
    # read the binary file and let the XMLRPC library encode it into base64
    with open(filename, 'rb') as img:
        data['bits'] = xmlrpc_client.Binary(img.read())
        response = wp.call(media.UploadFile(data))
        
    attachment_id = response['id']
        
    post.content = self.content    ##  post content

    post.post_status = self.status   ##post content

    terms_names1 = self.terms_names
    post.terms_names = self.terms_names  ##     ##The tag the article belongs to, if not, it will be automatically created

    wp.call(NewPost(post))
    