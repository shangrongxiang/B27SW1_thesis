from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.methods.posts import GetPosts, NewPost
from wordpress_xmlrpc.methods.users import GetUserInfo
from wordpress_xmlrpc.methods import posts
from wordpress_xmlrpc.methods import taxonomies
from wordpress_xmlrpc import WordPressTerm
from wordpress_xmlrpc.compat import xmlrpc_client
from wordpress_xmlrpc.methods import media, posts
from wordpress_xmlrpc import Client, WordPressPost

from wordpress_xmlrpc.methods.posts import GetPosts, NewPost

 
wp = Client('https://b27sw1.wordpress.com//xmlrpc.php', 'pecs107', '107srxsrx')
 
 
def post(title,content,status,terms_names):

    post = WordPressPost()

    post.title = title

    post.content = content

    post.post_status = status

    ##terms_names1 = {
   ## 'post_tag': ['test', 'firstpost'],

    ##'category': ['test']

    ##}
    terms_names1 = terms_names
    post.terms_names = terms_names

    wp.call(NewPost(post))