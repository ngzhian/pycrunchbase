=================================
NoneRelationship and NonePageItem
=================================

A :class:`NoneRelationship` is a subclass of :class:`Relationship` that represents a non-existent relationship. Think of it as a None that is also a Relationship.

A :class:`NoneRelationship` is returned by :meth:`_parse_relationship` in
:class:`Node`, when there is an expected relationship but it isn't in the returned data.

For example::

    members = organization.team_members  # the data we got from CrunchBase was missing the team_members realtionship
    assert instanceof(members[0], NoneRelationship) == True

The benefit of this is that calling the conventional relationship methods, such as :meth:`get`,
will return an object, rather than throwing an `AttributeError`::

    members = organization.team_members
    first_member = members.get(0)  # will not explode
    assert bool(first_member) == False

Because :class:`Relationship` are made up of :class:`PageItem`, we have a similar
`None` for it as well, called :class:`NonePageItem`. The idea behind it is similar to what
was discussed above as well::

    # continuing the example from above, we have member
    first_member = members.get(0)  # will not explode
    assert first_member.name == None
    assert first_member.whatever == None
