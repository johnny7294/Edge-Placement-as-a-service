ó
;(ë]c           @   s¢   d  d l  Z  d  d l Z d  d l Z d  d l Z d  d l m Z m Z e e  Z e j	 d d d g d    Z
 e d k r e j d e d	 d
 d d  n  d S(   iÿÿÿÿN(   t   Flaskt   requests   /json-examplet   methodst   POSTc       
   C   s
	  t  j d k r	t  j   }  d |  j   k rvxF|  d D]7} t |  d |  d j |  d  d } d | d } | d d k | t k @rt j d | d  i  } g  } | j |  | | d <t j	 |  } |  GHt
 j d d	 d
 | d d | g  } | j   d } | GHn  t GHd | d d | d }	 |	 GH| d d k |	 t k @rÕt j |	  i  } g  } | j |  | | d <t j	 |  } |  GHt
 j d d	 d
 | d d | g  } | j   d } | GHn  |	 d | d }
 |
 GH| d d k r8 i  } g  } | j |  | | d <t j	 |  } |  GHt
 j d d	 d
 | d d | g  } | j   d } | GHq8 q8 Wn  d |  j   k r	|  d d k rW|  d d k rWx¬ |  d D] } t |  d |  d j |  d  d } i  } g  } | j |  | | d <t j	 |  } t
 j d d	 d
 | d d d | g  } | j   d } | GHq³Wn  |  d d k r_|  d d k r_xÝ|  d D]Ñ} t |  d |  d j |  d  d } i  } g  } | j |  | | d <t j	 |  } t
 j d d	 d
 | d d d | g  } | j   d } | GHd | d GH| d d } | d j d  } | d j d   } t t | d!  d"  | d! <| d d  | d" d  | d# d  | d! } | GH| d | d" } | GH| | d <| | d <i  } g  } | j |  | | d <t j	 |  } t
 j d d	 d
 | d d d | g  } | j   d } | GHd$ | GHqWd% GHn  |  d d k r|  d d k rx	|  d D]ý } t |  d |  d j |  d  d } i  } g  } | j |  | | d <t j	 |  } t
 j d d	 d
 | d d d | g  } | j   d } | GH| d } t
 j d d& | g  } | j   d } d' } t
 j d d( | g  } | j   d } qWd) GHn  |  d d k r	|  d d k r	xJ|  d D];} t |  d |  d j |  d  d } i  } g  } | j |  | | d <t j	 |  } t
 j d d	 d
 | d d d | g  } | j   d } | GHd | d GH| d d } | d j d  } | d j d   } t t | d!  d"  | d! <| d d  | d" d  | d# d  | d! } | GH| d | d" } | GH| | d <| | d <i  } g  } | j |  | | d <t j	 |  } t
 j d d	 d
 | d d d | g  } | j   d } | GHd$ | GH| d } t
 j d d& | g  } | j   d } d' } t
 j d d( | g  } | j   d } d% GHd) GHq¾Wq	q	n  d* S(+   NR   t	   inputlistt   zones   .init   Tt   tidt    t   sudos   ansible-playbooks   -is   tenant_cont.ymls   -ei    t   Vt   vpcids   vpc_cont.ymlt   St   subids   subnet_cont.ymlt   guestst   reliablet   NOt   loggings   end_cont.ymls   -vvvt   YESs   IP of Edge: t   ipt   namet   Xt   /t   .i   i   i   s   IP of EdgeX: s    activating Reliablity s   ./pullaccesslog.shs    /home/ece792/samplepullscript.shs   ./addcronjob.shs    activating Logging s   building...(   R   t   methodt   get_jsont   keyst   strt   indext   tlistt   appendt   jsont   dumpst
   subprocesst   Popent   communicatet   vlistt   splitt   int(   t   req_datat   at   init   ot   datat   inyt   vart   p1t   outputt   vpt   sbt   guestt   guest2_namet   guest2_ip_listt   gt   kt	   guest2_ipR   t
   scriptpath(    (    s   control_center_final.pyt   json_example   s"   )
$
$
$ )
' )
'.


' )
'
 )
'.


'	
t   __main__t   debugt   hosts   0.0.0.0t   portiì  (   R!   R   t   ost	   ipaddresst   flaskR    R   t   __name__t   appt   routeR9   t   runt   True(    (    (    s   control_center_final.pyt   <module>   s   !