=================================
NoneRelationship and NonePageItem
=================================

A :class:`NoneRelationship` is a subclass of :class:`Relationship` that represents a non-existent relationship. Think of it as a None that is also a Relationship.

The benefit of this is that calling the conventional relationship methods, such as :meth:`get`,
will return an object, rather than throwing an `AttributeError`::

    rs = cb.more(organization.team_members)  # if rs is None
    assert bool(rs) === False
    rs.get(0)  # throws AttributeError: 'NoneType' object as no attribute 'get'

    rs = cb.more(organization.team_members)  # if rs is NoneRelationship
    assert bool(rs) === False
    member = rs.get(0)  # returns fine,
    assert bool(member) == False  # it's just a falsey value that returns more falsey values


My opinion is that it simplifies calls, rather than checking for `None` at each step,
you can just safely chain calls and check when you actually want the final object::

    rs = cb.more(organization.team_members)  # if rs is None
    if rs:
        member = rs.get(0)
        if member:
            print member

    # compared to
    rs = cb.more(organization.team_members)  # if rs is NoneRelationship
    member = cb.more(organization.team_members).get(0)
    if member:
        print member


A :class:`NoneRelationship` is returned by 2 methods in `pycrunchbase`,
:meth:`more` and :meth:`_parse_relationship`.

Because :class:`Relationship` are made up of :class:`PageItem`, we have a similar
`None` for it as well, called :class:`NonePageItem`. The idea behind it is similar to what
was discussed above as well::

    # continuing the example from above, we have member
    member = cb.more(organization.team_members).get(0)
    assert member.name == None
    assert member.whatever == None
