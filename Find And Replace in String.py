class Solution:
    def findReplaceString(self, s, inds, srcs, tgts):
        # it's in reverse because that way the changes don't affect each other
        for ind, src, tgt in sorted(zip(inds, srcs, tgts), reverse=True):
            # if the indicated part of the string that's the length of src is the same as src
            # change s to "s plus tgt + the part after src"
            # else do nothing
            s = s[:ind] + tgt + s[ind + len(src):] if s[ind:ind + len(src)] == src else s
        return s
        
