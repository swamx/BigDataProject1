# BigDataProject1
AMOD Big Data Course Data Collection Project 1: Collecting commits from git repository

The project aims to collect commits made on a GITHUB repository and be able to store those commits for analysis. 
This allows dataset users to analyse the information of message and conclude the importance of a commit.
For a large scale Open Source project thousands of commits are made everyday, the central body adopting certain branches for merge into master branch would want to view which branch has novel implementations that have been commited.
The term novel implementation includes changes in software such as code optimizations, introduction of new features, debugging, error corrections, and other minor or major changes.
A single commit has lots of information such as timestamp, owner of the repostiory, commiter information, and more. Most imortant information is the commit message which is a text message from commiter regarding changes he/she made. The messages are clear texts with details, hence there is no sentiment or sarcasm to detect. Thus, it becomes clear that the only relevant details in the commit message are terms and not the organization of the terms.

The storage solution used for storing commit is MongoDB because of the scalability and stability it offers. Apart from the same, it has been found that there is a need to convert the commit messages into SpaceVector Model before analysis. Previously, I (Devang Swami) had previsouly colaborated with my friend Chintan Raiyani to write a MapReduce code which find Tf-idf for documents after converting them to Space vector model. Interestingly MongoDB has support for the MapReduce Framework, its not so good with load balancing but still considerably good for this project which would be helpful when we wish to convert the data, since we would eradicate the need of moving the data to hadoop before analysis. Final advantage of MongoDB over other database's is the aggregation pipeline, which could be used for both data aggregation as well as for data enrichment (Especially Complex Enrichment).


Following is an example of a single commit:

{'_id': ObjectId('5a6651604166203a74c1ed7c'),
 'author': None,
 'comments_url': 'https://api.github.com/repos/torvalds/linux/commits/0d665e7b109d512b7cae3ccef6e8654714887844/comments',
 'commit': {'author': {'date': '2018-01-19T12:49:24Z',
                       'email': 'kirill.shutemov@linux.intel.com',
                       'name': 'Kirill A. Shutemov'},
            'comment_count': 0,
            'committer': {'date': '2018-01-22T01:44:47Z',
                          'email': 'torvalds@linux-foundation.org',
                          'name': 'Linus Torvalds'},
            'message': 'mm, page_vma_mapped: Drop faulty pointer arithmetics '
                       'in check_pte()\n'
                       '\n'
                       'Tetsuo reported random crashes under memory pressure '
                       'on 32-bit x86\n'
                       'system and tracked down to change that introduced\n'
                       'page_vma_mapped_walk().\n'
                       '\n'
                       'The root cause of the issue is the faulty pointer math '
                       'in check_pte().\n'
                       'As ->pte may point to an arbitrary page we have to '
                       'check that they are\n'
                       'belong to the section before doing math. Otherwise it '
                       'may lead to weird\n'
                       'results.\n'
                       '\n'
                       "It wasn't noticed until now as mem_map[] is virtually "
                       'contiguous on\n'
                       'flatmem or vmemmap sparsemem. Pointer arithmetic just '
                       'works against all\n'
                       "'struct page' pointers. But with classic sparsemem, it "
                       "doesn't because\n"
                       'each section memap is allocated separately and so '
                       'consecutive pfns\n'
                       'crossing two sections might have struct pages at '
                       'completely unrelated\n'
                       'addresses.\n'
                       '\n'
                       "Let's restructure code a bit and replace pointer "
                       'arithmetic with\n'
                       'operations on pfns.\n'
                       '\n'
                       'Signed-off-by: Kirill A. Shutemov '
                       '<kirill.shutemov@linux.intel.com>\n'
                       'Reported-and-tested-by: Tetsuo Handa '
                       '<penguin-kernel@i-love.sakura.ne.jp>\n'
                       'Acked-by: Michal Hocko <mhocko@suse.com>\n'
                       'Fixes: ace71a19cec5 ("mm: introduce '
                       'page_vma_mapped_walk()")\n'
                       'Cc: stable@vger.kernel.org\n'
                       'Signed-off-by: Linus Torvalds '
                       '<torvalds@linux-foundation.org>',
            'tree': {'sha': 'e6ebae5cd32b4f9008d06592a5301937c0be5875',
                     'url': 'https://api.github.com/repos/torvalds/linux/git/trees/e6ebae5cd32b4f9008d06592a5301937c0be5875'},
            'url': 'https://api.github.com/repos/torvalds/linux/git/commits/0d665e7b109d512b7cae3ccef6e8654714887844',
            'verification': {'payload': None,
                             'reason': 'unsigned',
                             'signature': None,
                             'verified': False}},
 'committer': {'avatar_url': 'https://avatars0.githubusercontent.com/u/1024025?v=4',
               'events_url': 'https://api.github.com/users/torvalds/events{/privacy}',
               'followers_url': 'https://api.github.com/users/torvalds/followers',
               'following_url': 'https://api.github.com/users/torvalds/following{/other_user}',
               'gists_url': 'https://api.github.com/users/torvalds/gists{/gist_id}',
               'gravatar_id': '',
               'html_url': 'https://github.com/torvalds',
               'id': 1024025,
               'login': 'torvalds',
               'organizations_url': 'https://api.github.com/users/torvalds/orgs',
               'received_events_url': 'https://api.github.com/users/torvalds/received_events',
               'repos_url': 'https://api.github.com/users/torvalds/repos',
               'site_admin': False,
               'starred_url': 'https://api.github.com/users/torvalds/starred{/owner}{/repo}',
               'subscriptions_url': 'https://api.github.com/users/torvalds/subscriptions',
               'type': 'User',
               'url': 'https://api.github.com/users/torvalds'},
 'html_url': 'https://github.com/torvalds/linux/commit/0d665e7b109d512b7cae3ccef6e8654714887844',
 'parents': [{'html_url': 'https://github.com/torvalds/linux/commit/0c5b9b5d9adbad4b60491f9ba0d2af38904bb4b9',
              'sha': '0c5b9b5d9adbad4b60491f9ba0d2af38904bb4b9',
              'url': 'https://api.github.com/repos/torvalds/linux/commits/0c5b9b5d9adbad4b60491f9ba0d2af38904bb4b9'}],
 'sha': '0d665e7b109d512b7cae3ccef6e8654714887844',
 'url': 'https://api.github.com/repos/torvalds/linux/commits/0d665e7b109d512b7cae3ccef6e8654714887844'}
