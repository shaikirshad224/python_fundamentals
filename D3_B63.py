#!/usr/bin/env python
# coding: utf-8

# In[15]:


#general syntax of f strings:

#f"custom words {placeholder1} {placeholder2}.....{placeholdern}"


# In[26]:


first_name='shaik'
last_name='irshad'


# In[27]:


full_name=f"{first_name} {last_name}"
print(full_name)


# In[28]:


print(full_name.title())


# In[29]:


print(f" keep up the good work,{full_name.title()}")


# In[31]:


Adding white spaces to the strings:


# In[32]:


print("favourite_language:pythonjavacswiftc++")


# In[ ]:





# In[33]:


print("favourite_language:\npython\njava\nc\nswift\nc++")


# In[35]:


#removing white spaces from strings:


# In[38]:


name1= 'python'


# In[39]:


print(name1)


# In[47]:


name2=' python'


# In[48]:


print(name2)


# In[49]:


name3='python '


# In[50]:


print(name1)


# In[51]:


print(name2)


# In[52]:


print(name3)


# In[53]:


name2.lstrip()


# In[54]:


name3.rstrip()


# In[55]:


name4="   python   "


# In[57]:


name4.strip()


# In[ ]:




